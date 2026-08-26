const puppeteer = require('puppeteer-core');
const https = require('https');
const fs = require('fs');
const path = require('path');

const handles = ['tecni_luispa', 'tecni_workout', 'tecniteam3x3'];

function downloadImage(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.instagram.com/' } }, res => {
      if (res.statusCode === 200) {
        res.pipe(file);
        file.on('finish', () => { file.close(); resolve(dest); });
      } else {
        file.close();
        fs.unlink(dest, () => {});
        reject(new Error(`HTTP ${res.statusCode}`));
      }
    }).on('error', err => {
      file.close();
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

async function scrapeProfilePhotos(browser, handle) {
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  await page.setViewport({ width: 1280, height: 900 });

  try {
    await page.goto(`https://www.instagram.com/${handle}/`, { waitUntil: 'networkidle2', timeout: 30000 });
    // Wait for images to load
    await new Promise(r => setTimeout(r, 5000));

    const data = await page.evaluate(() => {
      const imgs = Array.from(document.querySelectorAll('img'));
      const results = [];
      for (const img of imgs) {
        const src = img.src || img.dataset.src || '';
        if (!src) continue;
        // Profile picture: usually larger and near the top
        const isProfile = img.alt && (img.alt.includes('photo') || img.alt.includes('profile') || img.alt.includes('perfil'));
        // Post images: usually in grid
        const width = img.naturalWidth || img.width;
        const height = img.naturalHeight || img.height;
        results.push({ src, alt: img.alt || '', width, height, isProfile });
      }
      return results;
    });

    await page.close();
    return { handle, images: data };
  } catch(e) {
    await page.close();
    return { handle, error: e.message, images: [] };
  }
}

(async () => {
  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
  });

  const assetsDir = path.join(__dirname, 'assets');
  if (!fs.existsSync(assetsDir)) fs.mkdirSync(assetsDir);

  for (const handle of handles) {
    console.log(`\nScraping fotos de @${handle}...`);
    const { images, error } = await scrapeProfilePhotos(browser, handle);

    if (error) { console.log(`Error: ${error}`); continue; }

    console.log(`Encontradas ${images.length} imágenes`);

    // Filter meaningful images (skip tiny icons, skip instagram logos)
    const meaningful = images.filter(img =>
      img.src &&
      img.src.startsWith('https://') &&
      (img.src.includes('cdninstagram') || img.src.includes('fbcdn')) &&
      !img.src.includes('44x44') &&
      img.width > 50
    );

    console.log(`Filtrando: ${meaningful.length} imágenes de Instagram`);

    // Separate profile pic vs posts
    const sorted = meaningful.sort((a, b) => (b.width * b.height) - (a.width * a.height));

    // Download up to 10 images
    const toDownload = sorted.slice(0, 10);
    const downloaded = [];

    const handleDir = path.join(assetsDir, handle);
    if (!fs.existsSync(handleDir)) fs.mkdirSync(handleDir);

    for (let i = 0; i < toDownload.length; i++) {
      const img = toDownload[i];
      const ext = img.src.includes('.jpg') ? 'jpg' : img.src.includes('.png') ? 'png' : 'jpg';
      const filename = `${i === 0 ? 'profile' : `post_${i}`}.${ext}`;
      const dest = path.join(handleDir, filename);
      try {
        await downloadImage(img.src, dest);
        downloaded.push({ filename, local: `assets/${handle}/${filename}`, original: img.src, width: img.width, height: img.height });
        console.log(`✓ ${filename} (${img.width}x${img.height})`);
      } catch(e) {
        console.log(`✗ ${filename}: ${e.message}`);
      }
    }

    // Save manifest
    fs.writeFileSync(
      path.join(handleDir, 'manifest.json'),
      JSON.stringify(downloaded, null, 2)
    );
  }

  await browser.close();
  console.log('\nDone!');
})();
