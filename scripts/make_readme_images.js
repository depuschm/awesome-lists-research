// Screenshot the report page (docs/index.html) into README images, in light and dark themes.
// Usage: node scripts/make_readme_images.js   (needs Playwright with Chromium)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const root = path.resolve(__dirname, '..');
const out = path.join(root, 'assets', 'readme');
fs.mkdirSync(out, { recursive: true });
// Static images can't be hovered and already live on GitHub: drop those cues.
function staticCopy() {
  document.querySelectorAll('.fig-cap').forEach(c => { c.textContent = c.textContent.replace(' Hover for details.', ''); });
  const eb = document.querySelector('.hero .eyebrow');
  if (eb) eb.innerHTML = '<span class="tag">## research report</span> · data as of 25 October 2026';
}
const shots = { hero: 'header.hero', top100: '#fig-top100', dumbbell: '#fig-dumbbell', growth: '#fig-growth' };

(async () => {
  const browser = await chromium.launch();
  for (const scheme of ['light', 'dark']) {
    const page = await browser.newPage({ viewport: { width: 1180, height: 900 }, deviceScaleFactor: 2, colorScheme: scheme });
    await page.goto('file://' + path.join(root, 'docs', 'index.html'), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.evaluate(staticCopy);
    await page.addStyleTag({ content: '.hero{padding:46px 54px 40px!important;max-width:none!important;border-bottom:0!important}.hero .entry-line{display:none}' });
    await page.waitForTimeout(500);
    for (const [name, sel] of Object.entries(shots)) {
      const el = await page.$(sel);
      await el.screenshot({ path: path.join(out, `${name}-${scheme}.png`) });
    }
    // 1280x640 social preview card (Settings > General > Social preview)
    if (scheme === 'light') {
      const card = await browser.newPage({ viewport: { width: 1280, height: 640 }, deviceScaleFactor: 1, colorScheme: 'light' });
      await card.goto('file://' + path.join(root, 'docs', 'index.html'), { waitUntil: 'load' });
      await card.evaluate(() => document.fonts && document.fonts.ready);
      await card.evaluate(staticCopy);
      await card.addStyleTag({ content: '.article,.colophon{display:none}.hero{min-height:640px;box-sizing:border-box;align-content:center;padding-block:0;border:0}.entry-line{display:none}' });
      await card.waitForTimeout(300);
      await card.screenshot({ path: path.join(root, 'assets', 'social-preview.png'), clip: { x: 0, y: 0, width: 1280, height: 640 } });
      await card.close();
    }
    await page.close();
  }
  await browser.close();
  console.log(fs.readdirSync(out).join(' '));
})();
