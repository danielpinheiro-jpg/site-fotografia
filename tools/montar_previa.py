"""Monta uma prévia do site (site/dist) no formato de página do Claude (Artifact).

- CSS embutido no HTML, caminhos relativos (fotos/, marca/)
- index.html sem <html>/<head>/<body> (a plataforma acrescenta o esqueleto)
- en/index.html continua documento completo
Uso: python3 tools/montar_previa.py <pasta-saida>
"""
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIST = RAIZ / 'site/dist'
SAIDA = Path(sys.argv[1])


def preparar(html: str, prefixo: str, pt: str, en: str) -> str:
    def css(m):
        return '<style>' + (DIST / m.group(1).lstrip('/')).read_text() + '</style>'
    html = re.sub(r'<link rel="stylesheet" href="(/_astro/[^"]+\.css)">', css, html)
    html = re.sub(r'(["\s,])/(fotos|marca)/', rf'\1{prefixo}\2/', html)
    html = html.replace('href="/en/"', f'href="{en}"').replace('href="/"', f'href="{pt}"')
    return html


if SAIDA.exists():
    shutil.rmtree(SAIDA)
(SAIDA / 'en').mkdir(parents=True)

pagina = preparar((DIST / 'index.html').read_text(), '', '#topo', 'en/index.html')
cabeca = re.search(r'<head>(.*)</head>', pagina, re.S).group(1)
corpo = re.search(r'<body>(.*)</body>', pagina, re.S).group(1)
cabeca = re.sub(r'<meta charset[^>]*>|<meta name="viewport"[^>]*>', '', cabeca)
(SAIDA / 'index.html').write_text(cabeca + '\n' + corpo)

en = preparar((DIST / 'en/index.html').read_text(), '../', '../', '#topo')
(SAIDA / 'en/index.html').write_text(en)

shutil.copytree(DIST / 'fotos', SAIDA / 'fotos')
shutil.copytree(DIST / 'marca', SAIDA / 'marca')
print('ok', sum(1 for _ in SAIDA.rglob('*') if _.is_file()), 'arquivos')
