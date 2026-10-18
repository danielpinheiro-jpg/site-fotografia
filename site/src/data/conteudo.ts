/*
  Todo o texto do site, em português e inglês.
  Para mudar um texto, edite aqui — o resto do site se ajusta sozinho.
*/

export type Lang = 'pt' | 'en';

export const contato = {
  email: 'daniel.pinheiro@me.com',
  whatsapp: '+55 11 98346-3830',
  whatsappLink: 'https://wa.me/5511983463830',
  instagram: '@daniel_pinheiro_photography',
  instagramLink: 'https://www.instagram.com/daniel_pinheiro_photography/',
};

// Google Analytics 4: cole aqui o "ID da métrica" (começa com G-). Vazio = desligado.
export const analytics = {
  ga4: '',
};

// Ordem das seções de fotos no site (pasta em site/public/fotos/<id>)
export const temas = [
  { id: 'autoral',            pt: 'Autoral',              en: 'Personal Work' },
  { id: 'moda',               pt: 'Moda',                 en: 'Fashion' },
  { id: 'arquitetura',        pt: 'Arquitetura',          en: 'Architecture' },
  { id: 'publicidade',        pt: 'Publicidade',          en: 'Advertising' },
  { id: 'retratos',           pt: 'Retratos',             en: 'Portraits' },
] as const;

// Fotos da capa (nome do arquivo original) — passam em sequência, devagar.
// "foco" diz que parte da foto fica visível no celular (ex.: '50% 50%' = centro).
export const capa = [
  { tema: 'autoral', original: '_DSC2006_danielpinheiro©.jpg', foco: '45% 50%' },
  { tema: 'autoral', original: '_DSF3798_danielpinheiro©.jpg', foco: '62% 50%' },
  { tema: 'autoral', original: 'DSC_0080_danielpinheiro©.jpg', foco: '50% 50%' },
];

export const clientes = [
  'Fasano', 'Accor', 'Bourbon', 'Vivara', 'Melitta', 'Wella', 'Natura',
  'Cacau Show', 'Raia', 'MSD', 'Diageo', 'Sony & BMG', 'Tátil',
];

export const textos = {
  pt: {
    htmlLang: 'pt-BR',
    titulo: 'Daniel Pinheiro — Fotografia',
    descricao:
      'Portfólio do fotógrafo Daniel Pinheiro: autoral, moda, arquitetura, publicidade e retratos. São Paulo, Brasil.',
    pular: 'Pular para o conteúdo',
    menu: 'Menu',
    fechar: 'Fechar',
    sobre: 'Sobre',
    contato: 'Contato',
    fotos: 'fotos',
    anterior: 'Foto anterior',
    proxima: 'Próxima foto',
    verFoto: 'Ampliar foto',
    capaLegenda: 'Fotografia',
    clientes: 'Clientes',
    bioAbertura: 'Daniel Pinheiro',
    bio: [
      'Há mais de vinte anos, Daniel Pinheiro transforma luz em narrativa. Sua fotografia nasceu do encontro com o mestre Walter Firmo e se desenvolveu entre os retratos, a publicidade, a moda, a arquitetura, a gastronomia e os projetos documentais. Ao longo dessa trajetória, fotografou para marcas, revistas e instituições nacionais e internacionais, realizou exposições autorais e dirigiu a fotografia de filmes documentais, sempre mantendo um princípio que atravessa todo o seu trabalho: fotografar pessoas, lugares e objetos com o mesmo rigor estético e o mesmo respeito pelo que cada imagem representa.',
      'Sua assinatura está na luz natural, nas cores, nas texturas e na construção de imagens que revelam presença antes de espetáculo. Mais do que registrar cenas, Daniel busca criar fotografias que permaneçam relevantes com o passar do tempo, unindo precisão técnica, sensibilidade artística e narrativa visual.',
      'Hoje, reúne em uma única marca pessoal a experiência construída ao longo de mais de duas décadas de atuação, desenvolvendo projetos nas áreas de fotografia editorial, publicidade, arquitetura, hotelaria, gastronomia, retratos, documentário e fine art. Seu olhar permanece o mesmo, independentemente do cenário: encontrar a beleza, a verdade e a dignidade presentes em cada história.',
    ],
    retratoAlt: 'Retrato de Daniel Pinheiro em preto e branco',
    contatoTitulo: 'Vamos conversar',
    contatoTexto: 'Projetos, encomendas e licenciamento de imagens.',
    direitos: 'Todas as imagens © Daniel Pinheiro. Reprodução proibida sem autorização.',
    altFoto: (tema: string, n: number) => `${tema} — foto ${n} de Daniel Pinheiro`,
  },
  en: {
    htmlLang: 'en',
    titulo: 'Daniel Pinheiro — Photography',
    descricao:
      'Portfolio of photographer Daniel Pinheiro: personal work, fashion, architecture, advertising and portraits. São Paulo, Brazil.',
    pular: 'Skip to content',
    menu: 'Menu',
    fechar: 'Close',
    sobre: 'About',
    contato: 'Contact',
    fotos: 'photos',
    anterior: 'Previous photo',
    proxima: 'Next photo',
    verFoto: 'Enlarge photo',
    capaLegenda: 'Photography',
    clientes: 'Clients',
    bioAbertura: 'Daniel Pinheiro',
    bio: [
      'For more than twenty years, Daniel Pinheiro has been turning light into narrative. His photography was born from his encounter with the master Walter Firmo and grew across portraiture, advertising, fashion, architecture, food and documentary projects. Along the way he has photographed for brands, magazines and institutions in Brazil and abroad, held solo exhibitions and served as director of photography on documentary films — always guided by one principle that runs through all of his work: to photograph people, places and objects with the same aesthetic rigor and the same respect for what each image represents.',
      'His signature lies in natural light, in color, in texture, and in building images that reveal presence before spectacle. More than recording scenes, Daniel seeks to create photographs that remain relevant over time, combining technical precision, artistic sensibility and visual storytelling.',
      'Today he brings together, under a single personal brand, the experience of more than two decades of work, developing projects in editorial photography, advertising, architecture, hospitality, food, portraiture, documentary and fine art. His eye remains the same whatever the setting: to find the beauty, truth and dignity present in every story.',
    ],
    retratoAlt: 'Black and white portrait of Daniel Pinheiro',
    contatoTitulo: "Let's talk",
    contatoTexto: 'Commissions, projects and image licensing.',
    direitos: 'All images © Daniel Pinheiro. Reproduction prohibited without permission.',
    altFoto: (tema: string, n: number) => `${tema} — photo ${n} by Daniel Pinheiro`,
  },
};
