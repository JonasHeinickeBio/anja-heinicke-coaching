const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
  try {
    const siteRoot = path.resolve(process.cwd(), 'jekyll-site', '_site');
    const outDir = path.resolve(process.cwd(), 'screenshots');
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const pages = ['/', '/about/', '/retreat/', '/kontakt/'];
    for (const p of pages) {
      const target = p === '/' ? 'index.html' : path.join(p.replace(/^\//, ''), 'index.html');
      const fileUrl = 'file://' + path.join(siteRoot, target);
      const page = await browser.newPage();
      await page.setViewport({ width: 1280, height: 900 });
      await page.goto(fileUrl, { waitUntil: 'networkidle2' });
      const name = p === '/' ? 'index' : p.replace(/\//g, '') || 'page';
      const outPath = path.join(outDir, `${name}.png`);
      await page.screenshot({ path: outPath, fullPage: true });
      console.log('Wrote', outPath);
      await page.close();
    }
    await browser.close();
  } catch (e) {
    console.error(e);
    process.exit(1);
  }
})();
