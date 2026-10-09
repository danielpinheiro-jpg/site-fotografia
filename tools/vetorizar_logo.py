"""Vetoriza o logo (briefing/marca/logo-vertical.jpg) em SVGs para o site."""
import sys
import numpy as np
import potrace
from PIL import Image

SRC = 'briefing/marca/logo-vertical.jpg'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'site/public/marca'

im = np.asarray(Image.open(SRC).convert('RGB')).astype(int)
r, g, b = im[..., 0], im[..., 1], im[..., 2]
red = (r > 150) & (g < 110) & (b < 110)
black = (r < 110) & (g < 110) & (b < 110)


def paths(mask, x0, y0):
    bmp = potrace.Bitmap(~mask)  # potracer traça os pixels "falsos"
    curves = bmp.trace(turdsize=20, alphamax=1.0, opticurve=True, opttolerance=0.2)
    d = []
    for c in curves:
        s = c.start_point
        d.append(f'M{s.x - x0:.1f} {s.y - y0:.1f}')
        for seg in c.segments:
            if seg.is_corner:
                d.append(f'L{seg.c.x - x0:.1f} {seg.c.y - y0:.1f}L{seg.end_point.x - x0:.1f} {seg.end_point.y - y0:.1f}')
            else:
                d.append(f'C{seg.c1.x - x0:.1f} {seg.c1.y - y0:.1f} {seg.c2.x - x0:.1f} {seg.c2.y - y0:.1f} {seg.end_point.x - x0:.1f} {seg.end_point.y - y0:.1f}')
        d.append('Z')
    return ''.join(d)


def bbox(mask):
    ys, xs = np.nonzero(mask)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def svg(name, layers, box, title):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    body = ''.join(f'<path fill="{fill}" fill-rule="evenodd" d="{paths(m, x0, y0)}"/>' for m, fill in layers)
    open(f'{OUT}/{name}', 'w').write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')
    print(name, w, h)


# Monograma (parte de cima)
mono = red.copy(); mono[1300:] = False
svg('monograma-lp.svg', [(mono, 'var(--lp-red, #E22126)')], bbox(mono), 'Daniel Pinheiro')
open(f'{OUT}/favicon.svg', 'w').write(open(f'{OUT}/monograma-lp.svg').read().replace('var(--lp-red, #E22126)', '#E22126'))

# Assinatura horizontal (parte de baixo)
wr = red.copy(); wr[:1300] = False
wb = black.copy(); wb[:1300] = False
x0, y0, x1, y1 = bbox(wr | wb)
pad = 4
svg('assinatura.svg', [(wb, 'var(--lp-ink, #000)'), (wr, 'var(--lp-red, #E22126)')],
    (x0 - pad, y0 - pad, x1 + pad, y1 + pad), 'Daniel Pinheiro')

# Padrão de listras (versão vermelha), sem marcas de corte; o escuro vira preto
pad = np.asarray(Image.open('briefing/marca/padrao-listras-vermelho.jpg').convert('RGB')).astype(int)[206:1206, 220:1832]
pr, pg, pb = pad[..., 0], pad[..., 1], pad[..., 2]
p_red = (pr > 150) & (pg < 120) & (pb < 120)
p_dark = (pr < 120) & (pg < 120) & (pb < 120)
h, w = p_red.shape
body = ''.join(f'<path fill="{fill}" fill-rule="evenodd" d="{paths(m, 0, 0)}"/>' for m, fill in [(p_red, '#E22126'), (p_dark, '#000')])
open(f'{OUT}/listras.svg', 'w').write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" aria-hidden="true">{body}</svg>\n')
print('listras.svg', w, h)
