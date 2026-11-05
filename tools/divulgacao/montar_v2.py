# Doc Regenerar · Versão 2 (texto oficial): 3 carrosséis de 6 + stories
# Gera regenerar-v2.html; capas em 3 estilos (inteira, metades, faixas)
import re
base = open('regenerar.html').read()
css = re.search(r'<style>(.*?)</style>', base, re.S).group(1) + '''
  .faixa-a { position:absolute; left:0; width:1080px; object-fit:cover; }
  .metade { position:absolute; top:0; width:540px; object-fit:cover; }
  .corpo { font-size:30px; font-weight:300; line-height:1.45; color:rgba(30,35,32,.78); }
  .grande { font-family:'Cormorant Garamond',serif; font-weight:500; line-height:.9; color:var(--ocre); }
  .forte { background:linear-gradient(to top, rgba(18,22,19,.95) 0%, rgba(18,22,19,.8) 38%, rgba(18,22,19,.2) 62%, rgba(18,22,19,0) 75%) !important; }
'''
CREDITO = 'Direção de fotografia · Daniel Pinheiro'
P = []

def selo(top=80):
    return f'<div class="c selo" style="top:{top}px; left:80px;"><b>Regenerar</b> · Diários de uma imersão</div>'
def sombra(topo=True, forte=False, op=1):
    return f'<div class="sombra{" forte" if forte else ""}" style="opacity:{op}"></div>' + ('<div class="sombra-topo"></div>' if topo else '')
def foto(n, pos='50% 50%'):
    return f'<img class="foto" src="bayo/{n}.jpg" style="object-position:{pos}">'
def faixas(fs, H):
    h = H // 3
    return ''.join(f'<img class="faixa-a" src="bayo/{n}.jpg" style="top:{i*h}px; height:{h if i < 2 else H-2*h}px; object-position:{p}">' for i, (n, p) in enumerate(fs))
def metades(a, b, H):
    return (f'<img class="metade" src="bayo/{a[0]}.jpg" style="left:0; height:{H}px; object-position:{a[1]}">'
            f'<img class="metade" src="bayo/{b[0]}.jpg" style="left:540px; height:{H}px; object-position:{b[1]}">')
def num(n, claro=True):
    return f'<div class="c num" style="right:80px; bottom:70px;{"" if claro else " color:rgba(30,35,32,.6);"}">{n}</div>'
def bloco(titulo, sub='', tam=112, fundo=100, ital=False):
    i = ' font-style:italic;' if ital else ''
    s = f'<p class="sub" style="margin-top:26px;">{sub}</p>' if sub else ''
    return f'<div class="c" style="left:80px; right:80px; bottom:{fundo}px;"><span class="fio"></span><h1 class="titulo" style="font-size:{tam}px; margin-top:34px;{i}">{titulo}</h1>{s}</div>'
def legenda(txt, n):
    return f'<div class="c" style="left:80px; right:80px; bottom:80px; display:flex; justify-content:space-between; align-items:baseline;"><span class="legenda">{txt}</span><span class="num">{n}</span></div>'
def texto_osso(img, titulo, corpo, n):
    return (f'<img class="c" src="bayo/{img[0]}.jpg" style="left:0; top:0; width:1080px; height:620px; object-fit:cover; object-position:{img[1]};">'
            f'<div class="c" style="left:80px; right:80px; top:700px;"><span class="fio"></span><p class="titulo" style="font-size:64px; margin-top:30px;">{titulo}</p><p class="corpo" style="margin-top:30px;">{corpo}</p></div>' + num(n, False))
def fecho(titulo, linha, chamada):
    return ('<div class="c" style="left:80px; right:80px; top:120px;"><p class="selo" style="color:var(--tinta);">Regenerar · Diários de uma imersão</p></div>'
            f'<div class="c" style="left:80px; right:80px; top:380px;"><p class="titulo" style="font-size:104px; font-style:italic;">{titulo}</p><p style="font-size:32px; margin-top:40px; font-weight:400;">{linha}</p></div>'
            f'<div class="c" style="left:80px; right:80px; bottom:110px;"><span class="fio" style="background:var(--tinta)"></span><p style="font-size:30px; margin-top:28px; font-weight:500;">{chamada}</p><p style="font-size:24px; margin-top:12px; font-weight:300;">{CREDITO}</p></div>')
OSSO = ' style="background:var(--osso); color:var(--tinta);"'
SALVIA = ' style="background:var(--salvia); color:var(--tinta);"'
FILME = 'Times Are Urgent,<br>Let Us Slow Down'
def feed(i, html, extra=''): P.append(f'<section class="peca feed" id="{i}"{extra}>{html}</section>')
def story(i, html, extra=''): P.append(f'<section class="peca story" id="{i}"{extra}>{html}</section>')
def capas(post, titulo, sub, inteira, mets, fxs):
    t = bloco(titulo, sub)
    feed(f'{post}-01a', foto(*inteira) + sombra() + selo() + t)
    feed(f'{post}-01b', metades(*mets, 1350) + sombra() + selo() + t)
    feed(f'{post}-01c', faixas(fxs, 1350) + sombra() + selo() + t)

# ── POST 1 · Um filme nasce de muitos encontros (texto oficial)
capas('p1', 'Um filme nasce<br>de muitos encontros', 'Três dias com o filósofo Báyọ̀ Akómọláfé no interior de São Paulo.',
      (104, '50% 50%'), ((117, '47% 50%'), (129, '52% 50%')), [(85, '60% 22%'), (70, '55% 40%'), (98, '50% 30%')])
feed('p1-02', texto_osso((36, '50% 50%'), 'Desde 2018, nossos caminhos se cruzam com os de Báyọ̀ Akómọláfé.', 'Desses encontros nasceram uma parceria criativa e uma amizade.', '02'), OSSO)
feed('p1-03', metades((73, '62% 50%'), (53, '40% 50%'), 1350) + sombra(topo=False) + bloco('Produções, debates, viagens<br>e muitas conversas.', tam=72, fundo=110) + num('03'))
feed('p1-04', texto_osso((75, '50% 50%'), 'Três dias de imersão para criar o nosso novo longa-metragem.', 'O cinema como forma de fazer circular ideias que deslocam nossas certezas sobre o mundo.', '04'), OSSO)
feed('p1-05', faixas([(121, '40% 50%'), (124, '50% 50%'), (137, '40% 45%')], 1350) + sombra(topo=False) + bloco('Uma nova etapa: construção<br>narrativa e pós-produção.', tam=72, fundo=110) + num('05'))
feed('p1-06', fecho(FILME, 'Novo longa-metragem · estreia em 2027', 'Conheça a jornada e apoie o filme: link na bio'), SALVIA)

# ── POST 2 · Báyọ̀ Akómọláfé (rascunho a validar com a equipe)
capas('p2', 'Báyọ̀<br>Akómọláfé', 'Filósofo nigeriano, parceiro do Regenerar desde 2018.',
      (126, '36% 50%'), ((98, '40% 50%'), (118, '52% 50%')), [(5, '45% 40%'), (61, '50% 40%'), (128, '62% 45%')])
feed('p2-02', f'<img class="c" src="bayo/58.jpg" style="left:80px; top:110px; width:420px; height:520px; object-fit:cover; object-position:30% 50%;">'
     '<div class="c" style="left:80px; right:80px; top:700px;"><p class="titulo" style="font-size:96px; font-style:italic;">“Times are urgent,<br>let us slow down.”</p>'
     '<p class="legenda" style="margin-top:40px; color:var(--salvia);">Báyọ̀ Akómọláfé</p><p class="sub" style="margin-top:16px; font-size:28px;">A frase que dá nome ao novo filme.</p></div>' + num('02'))
feed('p2-03', foto(117, '47% 50%') + sombra(topo=False, op=.85) + legenda('No jardim da casa', '03'))
feed('p2-04', faixas([(113, '50% 35%'), (6, '45% 40%'), (61, '40% 40%')], 1350) + sombra(topo=False) + bloco('Conversas que deslocam<br>nossas certezas.', tam=72, fundo=110) + num('04'))
feed('p2-05', foto(128, '66% 50%') + sombra(topo=False, op=.6) + legenda('', '05'))
feed('p2-06', fecho(FILME, 'Já conquistamos cerca de 60% dos recursos da pós-produção.', 'Ajude a levar o filme ao mundo em 2027: link na bio'), SALVIA)

# ── POST 3 · Pensar junto / bastidores (rascunho)
capas('p3', 'Pensar<br>junto', 'Os bastidores de um filme ainda em construção.',
      (133, '50% 50%'), ((132, '22% 50%'), (85, '55% 50%')), [(19, '50% 40%'), (27, '55% 40%'), (64, '45% 40%')])
feed('p3-02', foto(129, '50% 40%') + sombra(topo=False, op=.85) + legenda('', '02'))
feed('p3-03', metades((125, '55% 50%'), (64, '52% 50%'), 1350) + sombra(topo=False) + bloco('Cada porta,<br>uma pergunta.', tam=80, fundo=110) + num('03'))
feed('p3-04', foto(137, '45% 50%') + sombra(topo=False, op=.6) + legenda('As “portas” do roteiro', '04'))
feed('p3-05', texto_osso((27, '50% 40%'), 'Fotografar um filme enquanto ele ainda está sendo pensado.', 'Registrar o processo: as conversas, as dúvidas, os gestos de quem constrói junto.', '05'), OSSO)
feed('p3-06', fecho(FILME, 'Novo longa-metragem · estreia em 2027', 'Acompanhe e apoie o filme: link na bio'), SALVIA)

# ── STORIES
def st(i, html, extra=''): story(i, html + selo(150), extra)
st('s01', foto(117, '47% 50%') + sombra() + bloco('Um filme nasce<br>de muitos<br>encontros', 'Diários de uma imersão com Báyọ̀ Akómọláfé. Novo post no perfil.', 120, 260))
st('s02', metades((5, '52% 50%'), (85, '50% 50%'), 1920) + sombra() + bloco('Três dias.<br>Um novo filme.', 'Imersão de criação no interior de São Paulo.', 120, 260))
st('s03', foto(27, '55% 50%') + sombra() + bloco('Fotografei esta<br>imersão.', f'{CREDITO}<br>no novo longa do Regenerar.', 120, 260))
st('s04', foto(126, '36% 50%') + sombra(forte=True) + bloco('“Times are urgent,<br>let us slow down.”', 'Báyọ̀ Akómọláfé', 104, 260, ital=True))
st('s05', faixas([(104, '50% 50%'), (121, '40% 50%'), (133, '50% 50%')], 1920) + sombra() + bloco(FILME, 'Novo longa-metragem · estreia em 2027', 112, 260, ital=True))
st('s06', foto(129, '50% 40%') + sombra(forte=True) + '<div class="c" style="left:80px; right:80px; bottom:260px;"><p class="grande" style="font-size:300px;">60%</p><p class="titulo" style="font-size:72px; margin-top:10px;">dos recursos da pós-produção<br>já conquistados.</p><p class="sub" style="margin-top:28px;">Ajude a levar o filme ao mundo em 2027.<br>Link na bio.</p></div>')
st('s07', foto(98, '45% 40%') + sombra(forte=True) + '<div class="c" style="left:80px; right:80px; top:1060px;"><h1 class="titulo" style="font-size:100px;">Você conhece<br>Báyọ̀ Akómọláfé?</h1><p class="sub" style="margin-top:26px;">[espaço para o adesivo de enquete]</p></div>')
st('s08', faixas([(113, '50% 35%'), (75, '50% 50%'), (64, '45% 40%')], 1920) + sombra() + bloco('Três posts<br>no meu perfil.', 'A imersão · Báyọ̀ Akómọláfé · Pensar junto', 120, 260))

head = base[:base.index('<style>')]
open('regenerar-v2.html', 'w').write(head + '<style>' + css + '</style></head><body>\n' + '\n'.join(P) +
     '\n<script>document.fonts.ready.then(()=>document.body.dataset.pronto="1")</script></body></html>')
print(len(P), 'peças')
