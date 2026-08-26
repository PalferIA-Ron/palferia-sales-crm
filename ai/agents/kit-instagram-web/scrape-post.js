const puppeteer = require('puppeteer-core');
const https = require('https');
const fs = require('fs');
const path = require('path');

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
    }).on('error', err => { file.close(); reject(err); });
  });
}

(async () => {
  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  await page.setViewport({ width: 1280, height: 900 });

  await page.goto('https://www.instagram.com/p/DYpK27_tKJX/', { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));

  const images = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('img')).map(img => ({
      src: img.src,
      alt: img.alt,
      width: img.naturalWidth || img.width,
      height: img.naturalHeight || img.height
    })).filter(i => i.src && (i.src.includes('cdninstagram') || i.src.includes('fbcdn')));
  });

  await browser.close();

  console.log('Imágenes encontradas:');
  images.forEach((img, i) => console.log(`${i}: ${img.width}x${img.height} — ${img.src.substring(0, 80)}...`));

  // Get the largest image
  const sorted = images.sort((a, b) => (b.width * b.height) - (a.width * a.height));
  const best = sorted[0];

  if (best) {
    const dest = path.join(__dirname, 'assets', 'tecni_luispa', 'ceo.jpg');
    await downloadImage(best.src, dest);
    console.log(`\n✓ Descargada: ${dest}`);
  } else {
    console.log('No se encontró imagen');
  }
})();
