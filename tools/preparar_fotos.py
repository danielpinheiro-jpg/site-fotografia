"""Prepara as fotos para o site.

Lê  fotos-originais/<tema>/*.jpg  (cópias do Dropbox, fora do git)
Gera site/public/fotos/<tema>/NN-<largura>.webp em 3 tamanhos
e site/src/data/fotos.json com a ordem, proporção e nome original.

A ordem segue site/src/data/ordem.json quando existir (lista de nomes
originais por tema); fotos novas entram no fim, em ordem alfabética.
"""
import json
import os
from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
ORIGEM = Path(os.environ.get('FOTOS_ORIGEM', RAIZ / 'fotos-originais'))
DESTINO = RAIZ / 'site/public/fotos'
DADOS = RAIZ / 'site/src/data'
TEMAS = ['autoral', 'moda', 'arquitetura-hoteis', 'publicidade', 'retratos']
LARGURAS = [800, 1600, 2400]

ordem_path = DADOS / 'ordem.json'
ordem = json.loads(ordem_path.read_text()) if ordem_path.exists() else {}
manifesto = {}

for tema in TEMAS:
    pasta = ORIGEM / tema
    arquivos = sorted(p.name for p in pasta.glob('*.jp*g')) if pasta.exists() else []
    preferida = [n for n in ordem.get(tema, []) if n in arquivos]
    arquivos = preferida + [n for n in arquivos if n not in preferida]
    ordem[tema] = arquivos
    saida = DESTINO / tema
    saida.mkdir(parents=True, exist_ok=True)
    for velho in saida.glob('*.webp'):
        velho.unlink()
    itens = []
    for i, nome in enumerate(arquivos, 1):
        im = ImageOps.exif_transpose(Image.open(pasta / nome)).convert('RGB')
        w, h = im.size
        base = f'{i:02d}'
        for largura in LARGURAS:
            alvo = min(largura, w)
            copia = im if alvo == w else im.resize((alvo, round(h * alvo / w)), Image.LANCZOS)
            copia.save(saida / f'{base}-{largura}.webp', 'WEBP', quality=82, method=6)
        itens.append({'id': base, 'w': w, 'h': h, 'original': nome})
    manifesto[tema] = itens
    print(f'{tema}: {len(itens)} fotos')

DADOS.mkdir(parents=True, exist_ok=True)
(DADOS / 'fotos.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n')
ordem_path.write_text(json.dumps(ordem, ensure_ascii=False, indent=2) + '\n')
