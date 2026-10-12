import { defineConfig } from 'astro/config';

// SITE_URL e BASE_PATH permitem montar a prévia em outro endereço
// (ex.: GitHub Pages em /site-fotografia). Sem eles, vale o domínio próprio.
export default defineConfig({
  site: process.env.SITE_URL || 'https://danielpinheiro.com.br',
  base: process.env.BASE_PATH || '/',
  compressHTML: true,
});
