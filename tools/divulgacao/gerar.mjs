// Gera as imagens das peças (JPG) a partir de pecas.html.
// Antes: node tools/divulgacao/telas.mjs <url-do-site> tools/divulgacao/telas
// Uso:   node tools/divulgacao/gerar.mjs <pasta-saida> [pagina.html]  (padrão: pecas.html)   (servindo a raiz do repositório em localhost:8767)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const out = process.argv[2];
const pagina = process.argv[3] || 'pecas.html';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1300, height: 2100 } });
await p.goto(`http://localhost:8767/tools/divulgacao/${pagina}`, { waitUntil: 'networkidle' });
await p.waitForSelector('body[data-pronto]');
await p.evaluate(() => document.fonts.ready);
for (const id of await p.$$eval('.peca', (els) => els.map((e) => e.id))) {
  await p.locator('#' + id).screenshot({ path: `${out}/${id}.jpg`, type: 'jpeg', quality: 92 });
  console.log(id);
}
await b.close();
