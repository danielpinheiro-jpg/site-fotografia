// Tira "recortes" do site (celular e computador) para usar nas peças de divulgação.
// Uso: node tools/divulgacao/telas.mjs <url-do-site> <pasta-saida>
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [url, out] = process.argv.slice(2);
const b = await chromium.launch();
const ir = async (p, id) => {
  await p.evaluate((i) => { document.documentElement.style.scrollBehavior = 'auto'; if (i) document.getElementById(i).scrollIntoView(); else scrollTo(0, 0); }, id);
  await p.evaluate(() => document.querySelectorAll('img[loading="lazy"]').forEach((i) => (i.loading = 'eager')));
  await p.waitForTimeout(2500);
};
const cel = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
await cel.goto(url, { waitUntil: 'networkidle' });
for (const [nome, id, extra] of [['cel-capa', null, 0], ['cel-autoral', 'autoral', 0], ['cel-moda', 'moda', 330], ['cel-arquitetura', 'arquitetura', 0], ['cel-sobre', 'sobre', 0]]) {
  await ir(cel, id); if (extra) { await cel.evaluate((y) => scrollBy(0, y), extra); await cel.waitForTimeout(1500); }
  await cel.screenshot({ path: `${out}/${nome}.png` });
}
const pc = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
await pc.goto(url, { waitUntil: 'networkidle' });
for (const [nome, id] of [['pc-capa', null], ['pc-moda', 'moda']]) { await ir(pc, id); await pc.screenshot({ path: `${out}/${nome}.png` }); }
await b.close();
