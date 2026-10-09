/*
  Interações do site: topo que muda ao sair da capa, menu do celular,
  capa com fotos alternando, fotos que surgem ao rolar e o visualizador
  de fotos em tela cheia (setas do teclado e deslizar do dedo).
*/

const reduzido = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// ── Topo: transparente sobre a capa, branco no resto ──
const topo = document.querySelector<HTMLElement>('[data-topo]');
const capa = document.querySelector<HTMLElement>('[data-capa]');
if (topo && capa) {
  const atualizar = () => topo.classList.toggle('sobre-capa', window.scrollY < capa.offsetHeight - topo.offsetHeight);
  window.addEventListener('scroll', atualizar, { passive: true });
  atualizar();
}

// ── Item do menu ativo conforme a seção na tela ──
const linksNav = [...document.querySelectorAll<HTMLAnchorElement>('[data-nav]')];
const secoes = linksNav
  .map((a) => document.querySelector<HTMLElement>(a.getAttribute('href')!))
  .filter((s): s is HTMLElement => !!s);
const observadorNav = new IntersectionObserver(
  (entradas) => {
    for (const e of entradas) {
      if (!e.isIntersecting) continue;
      for (const a of linksNav) a.setAttribute('aria-current', String(a.getAttribute('href') === `#${e.target.id}`));
    }
  },
  { rootMargin: '-45% 0px -50% 0px' },
);
secoes.forEach((s) => observadorNav.observe(s));

// ── Menu do celular ──
const menu = document.querySelector<HTMLElement>('[data-menu]');
const abrir = document.querySelector<HTMLButtonElement>('[data-abrir-menu]');
function fecharMenu() {
  if (!menu || !abrir) return;
  menu.classList.remove('aberto');
  abrir.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
  setTimeout(() => { if (!menu.classList.contains('aberto')) menu.hidden = true; }, 350);
}
abrir?.addEventListener('click', () => {
  if (!menu) return;
  menu.hidden = false;
  requestAnimationFrame(() => menu.classList.add('aberto'));
  abrir.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
  menu.querySelector<HTMLElement>('button')?.focus();
});
document.querySelectorAll('[data-fechar-menu]').forEach((el) => el.addEventListener('click', fecharMenu));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && menu?.classList.contains('aberto')) fecharMenu(); });

// ── Capa: fotos alternando devagar ──
const fotosCapa = [...document.querySelectorAll<HTMLImageElement>('.capa__foto')];
if (fotosCapa.length > 1 && !reduzido) {
  let atual = 0;
  setInterval(() => {
    if (document.hidden) return;
    fotosCapa[atual].classList.remove('ativa');
    atual = (atual + 1) % fotosCapa.length;
    fotosCapa[atual].classList.add('ativa');
  }, 6000);
}

// ── Elementos surgem ao rolar ──
const surgir = new IntersectionObserver(
  (entradas) => {
    for (const e of entradas) {
      if (e.isIntersecting) {
        e.target.classList.add('visivel');
        surgir.unobserve(e.target);
      }
    }
  },
  { rootMargin: '0px 0px -8% 0px' },
);
document.querySelectorAll('.surgir').forEach((el) => surgir.observe(el));

// ── Visualizador de fotos ──
const visor = document.querySelector<HTMLDialogElement>('[data-visor]');
const img = document.querySelector<HTMLImageElement>('[data-visor-img]');
const conta = document.querySelector<HTMLElement>('[data-visor-conta]');
const rotuloTema = document.querySelector<HTMLElement>('[data-visor-tema]');
let botoes: HTMLButtonElement[] = [];
let indice = 0;
let origem: HTMLElement | null = null;

function mostrar(i: number) {
  if (!img || !conta) return;
  indice = (i + botoes.length) % botoes.length;
  const b = botoes[indice];
  img.classList.add('carregando');
  img.onload = () => img.classList.remove('carregando');
  img.srcset = b.dataset.srcset ?? '';
  img.sizes = '100vw';
  img.src = b.dataset.foto ?? '';
  img.alt = b.querySelector('img')?.alt ?? '';
  conta.innerHTML = `<b>${String(indice + 1).padStart(2, '0')}</b> / ${String(botoes.length).padStart(2, '0')}`;
  // Pré-carrega a próxima
  const prox = botoes[(indice + 1) % botoes.length];
  const pre = new Image();
  pre.sizes = '100vw';
  pre.srcset = prox.dataset.srcset ?? '';
}

document.querySelectorAll<HTMLUListElement>('[data-galeria]').forEach((galeria) => {
  const titulo = galeria.closest('section')?.querySelector('h2')?.lastChild?.textContent?.trim() ?? '';
  const lista = [...galeria.querySelectorAll<HTMLButtonElement>('button')];
  lista.forEach((b, i) =>
    b.addEventListener('click', () => {
      if (!visor) return;
      botoes = lista;
      origem = b;
      if (rotuloTema) rotuloTema.textContent = titulo;
      mostrar(i);
      visor.showModal();
      document.body.style.overflow = 'hidden';
    }),
  );
});

visor?.addEventListener('close', () => {
  document.body.style.overflow = '';
  origem?.focus();
});
document.querySelector('[data-visor-fechar]')?.addEventListener('click', () => visor?.close());
document.querySelector('[data-visor-ant]')?.addEventListener('click', () => mostrar(indice - 1));
document.querySelector('[data-visor-prox]')?.addEventListener('click', () => mostrar(indice + 1));
visor?.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') mostrar(indice - 1);
  if (e.key === 'ArrowRight') mostrar(indice + 1);
});

// Deslizar o dedo no celular
const palco = document.querySelector<HTMLElement>('[data-visor-palco]');
let toqueX = 0;
palco?.addEventListener('touchstart', (e) => { toqueX = e.touches[0].clientX; }, { passive: true });
palco?.addEventListener('touchend', (e) => {
  const dx = e.changedTouches[0].clientX - toqueX;
  if (Math.abs(dx) > 50) mostrar(indice + (dx < 0 ? 1 : -1));
});
