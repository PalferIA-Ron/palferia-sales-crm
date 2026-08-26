const puppeteer = require('puppeteer-core');

const handles = ['tecni_luispa', 'tecni_workout', 'tecniteam3x3'];

async function scrapeProfile(browser, handle) {
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

  try {
    await page.goto(`https://www.instagram.com/${handle}/`, { waitUntil: 'networkidle2', timeout: 30000 });
    await new Promise(r => setTimeout(r, 3000));

    const data = await page.evaluate(() => {
      // Try to get data from meta tags and page content
      const metas = {};
      document.querySelectorAll('meta').forEach(m => {
        if (m.name || m.property) metas[m.name || m.property] = m.content;
      });

      // Try to find JSON data in scripts
      let jsonData = null;
      document.querySelectorAll('script[type="application/ld+json"]').forEach(s => {
        try { jsonData = JSON.parse(s.textContent); } catch(e) {}
      });

      // Try window._sharedData
      let sharedData = null;
      try {
        const scripts = Array.from(document.querySelectorAll('script:not([src])'));
        for (const s of scripts) {
          if (s.textContent.includes('window._sharedData')) {
            const match = s.textContent.match(/window\._sharedData\s*=\s*({.+?});/);
            if (match) sharedData = JSON.parse(match[1]);
          }
        }
      } catch(e) {}

      return {
        title: document.title,
        description: metas['description'] || metas['og:description'] || '',
        image: metas['og:image'] || '',
        jsonData,
        sharedData: sharedData ? JSON.stringify(sharedData).substring(0, 2000) : null,
        bodyText: document.body.innerText.substring(0, 3000)
      };
    });

    await page.close();
    return { handle, ...data };
  } catch(e) {
    await page.close();
    return { handle, error: e.message };
  }
}

(async () => {
  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
  });

  const results = [];
  for (const handle of handles) {
    console.log(`Scraping @${handle}...`);
    const result = await scrapeProfile(browser, handle);
    results.push(result);
  }

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();
