# Guia de Design UX - MVP 3

**Referência visual consolidada para implementação do MVP 3**

---

## 🎨 Visão Geral

Este documento consolida todas as decisões de design UX moderno para o MVP 3 do portfolio.

### Objetivos:
1. Visual moderno e profissional (tendências 2025)
2. UX intuitiva e acessível
3. Foco em conversão (CTAs estratégicos)
4. Performance e responsividade

---

## 📐 Layout Estrutural Completo

```
┌──────────────────────────────────────────────────────────────┐
│                    NAVBAR (fixed top)                        │
│  Logo    [Home] [Sobre] [Skills] [Projetos] [Contato]   ☰  │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    HERO SECTION                              │
│                  (gradient background)                       │
│                                                              │
│                    ┌─────────────┐                          │
│                    │             │                          │
│                    │    FOTO     │                          │
│                    │  (circular) │                          │
│                    └─────────────┘                          │
│                                                              │
│              Olá, sou Ésley Nathan 👋                       │
│          Desenvolvedor Full-Stack Python                    │
│                                                              │
│     "Construindo aplicações web escaláveis e modernas       │
│          com Django, Angular e boas práticas"               │
│                                                              │
│        ┌──────────────┐   ┌──────────────┐                │
│        │Ver Projetos ↓│   │Download CV 📄│                │
│        └──────────────┘   └──────────────┘                │
│                                                              │
│           [GitHub] [LinkedIn] [Email]                       │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    SOBRE MIM                                 │
│                  (background: white)                         │
│                                                              │
│  ┌────────────────┬───────────────────────────────────────┐ │
│  │                │                                       │ │
│  │   ┌────────┐   │   Desenvolvedor Full-Stack Python... │ │
│  │   │        │   │                                       │ │
│  │   │  FOTO  │   │   Engenheiro de Computação...        │ │
│  │   │ PROFILE│   │                                       │ │
│  │   │        │   │   Experiência em desenvolvimento...  │ │
│  │   └────────┘   │                                       │ │
│  │   256x256px    │   [4 parágrafos do CV atual]         │ │
│  │                │                                       │ │
│  └────────────────┴───────────────────────────────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    SKILLS                                    │
│              (background: bg-gray-50)                        │
│                                                              │
│                  Habilidades Técnicas                        │
│                                                              │
│  ┌─ Frontend ──────────────────────────────────────────┐   │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐           │   │
│  │  │  🅰️  │  │  ⚛️  │  │  📘  │  │  🎨  │           │   │
│  │  │Angular│  │React │  │ TS   │  │Tailwind│         │   │
│  │  │ ████░ │  │ ███░░ │  │ ████░ │  │ ████░ │         │   │
│  │  └──────┘  └──────┘  └──────┘  └──────┘           │   │
│  └────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─ Backend ───────────────────────────────────────────┐   │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐           │   │
│  │  │  🐍  │  │  🎯  │  │  🔥  │  │  🗄️  │           │   │
│  │  │Python│  │Django│  │Flask │  │ SQL  │           │   │
│  │  │█████ │  │█████ │  │ ████░ │  │ ████░ │         │   │
│  │  └──────┘  └──────┘  └──────┘  └──────┘           │   │
│  └────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─ DevOps & Ferramentas ─────────────────────────────┐   │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐           │   │
│  │  │  🐳  │  │  📦  │  │  🔧  │  │  🌿  │           │   │
│  │  │Docker│  │ Git  │  │Linux │  │Nginx │           │   │
│  │  │ ████░ │  │█████ │  │ ████░ │  │ ███░░ │        │   │
│  │  └──────┘  └──────┘  └──────┘  └──────┘           │   │
│  └────────────────────────────────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    PROJETOS                                  │
│                  (background: white)                         │
│                                                              │
│                  Projetos em Destaque                        │
│                                                              │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│
│  │ ┌────────────┐ │  │ ┌────────────┐ │  │ ┌────────────┐ ││
│  │ │   IMAGE    │ │  │ │   IMAGE    │ │  │ │   IMAGE    │ ││
│  │ └────────────┘ │  │ └────────────┘ │  │ └────────────┘ ││
│  │                │  │                │  │                ││
│  │ ⭐ FEATURED    │  │ Project Title  │  │ Project Title  ││
│  │ Project Title  │  │                │  │                ││
│  │                │  │ Description... │  │ Description... ││
│  │ Description... │  │                │  │                ││
│  │                │  │ [Python][DRF]  │  │ [Angular][TS]  ││
│  │ [Django][Ang]  │  │                │  │                ││
│  │                │  │ [GitHub] [Demo]│  │ [GitHub] [Demo]││
│  │ [GitHub] [Demo]│  │                │  │                ││
│  │                │  │                │  │                ││
│  └────────────────┘  └────────────────┘  └────────────────┘│
│                                                              │
│                [Ver Todos os Projetos]                       │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    CONTATO                                   │
│              (background: bg-primary-50)                     │
│                                                              │
│              Vamos trabalhar juntos? 🚀                      │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  [Nome]                                                │ │
│  │  ─────────────────────────────────                     │ │
│  │                                                        │ │
│  │  [Email]                                               │ │
│  │  ─────────────────────────────────                     │ │
│  │                                                        │ │
│  │  [Assunto]                                             │ │
│  │  ─────────────────────────────────                     │ │
│  │                                                        │ │
│  │  [Mensagem]                                            │ │
│  │  ┌────────────────────────────────────────────────┐   │ │
│  │  │                                                │   │ │
│  │  │                                                │   │ │
│  │  └────────────────────────────────────────────────┘   │ │
│  │                                                        │ │
│  │              ┌────────────────────┐                    │ │
│  │              │  Enviar Mensagem  │                    │ │
│  │              └────────────────────┘                    │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    FOOTER                                    │
│              (background: bg-gray-900)                       │
│                                                              │
│              Ésley Nathan © 2025                            │
│         Desenvolvedor Full-Stack Python                     │
│                                                              │
│           [GitHub] [LinkedIn] [Email]                       │
│                                                              │
│       Desenvolvido com Django + Angular + Tailwind          │
│                                                              │
└──────────────────────────────────────────────────────────────┘

                    ┌───────────┐
                    │    ↑      │  ← Botão "Voltar ao Topo"
                    │  Topo     │     (fixed bottom-right)
                    └───────────┘
```

---

## 🎨 Paleta de Cores

### Cores Principais (já configuradas no Tailwind)

```css
Primary (Azul):
- primary-50:  #eff6ff  /* backgrounds sutis */
- primary-100: #dbeafe  /* borders, highlights */
- primary-600: #2563eb  /* botões, links */
- primary-700: #1d4ed8  /* hover states */
- primary-900: #1e3a8a  /* textos escuros */

Neutros:
- gray-50:  #f9fafb   /* backgrounds alternados */
- gray-100: #f3f4f6   /* borders */
- gray-600: #4b5563   /* textos secundários */
- gray-700: #374151   /* textos principais */
- gray-900: #111827   /* footer, textos escuros */

Estados:
- green-500: #10b981  /* success */
- red-500:   #ef4444  /* errors */
- yellow-500: #f59e0b /* warnings */
```

### Gradientes

```css
/* Hero Background */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* ou */
background: linear-gradient(to right, #2563eb, #3b82f6, #60a5fa);

/* Text Gradient (títulos) */
background: linear-gradient(to right, #2563eb, #7c3aed);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

---

## 🔤 Tipografia

### Hierarquia de Texto

```css
/* Hero - Título Principal */
.hero-title {
  font-size: 3.75rem;    /* text-6xl */
  font-weight: 800;      /* font-extrabold */
  line-height: 1;        /* leading-none */
  letter-spacing: -0.025em;
}

/* Hero - Subtítulo */
.hero-subtitle {
  font-size: 1.5rem;     /* text-2xl */
  font-weight: 600;      /* font-semibold */
  color: #4b5563;        /* text-gray-600 */
}

/* Section Titles */
.section-title {
  font-size: 2.25rem;    /* text-4xl */
  font-weight: 700;      /* font-bold */
  color: #111827;        /* text-gray-900 */
}

/* Card Titles */
.card-title {
  font-size: 1.25rem;    /* text-xl */
  font-weight: 700;      /* font-bold */
  color: #111827;
}

/* Body Text */
.body-text {
  font-size: 1.125rem;   /* text-lg */
  line-height: 1.75rem;  /* leading-relaxed */
  color: #374151;        /* text-gray-700 */
}
```

---

## 🖼️ Componentes Detalhados

### 1. Hero Section

```html
<section id="hero" class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-600 via-primary-700 to-purple-800 text-white relative overflow-hidden">
  <!-- Background Pattern (opcional) -->
  <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>

  <div class="container mx-auto px-4 text-center relative z-10">
    <!-- Foto de Perfil -->
    <div class="mb-8 animate-fade-in">
      <img
        src="assets/images/profile.jpg"
        alt="Ésley Nathan"
        class="w-48 h-48 md:w-56 md:h-56 rounded-full mx-auto object-cover border-4 border-white shadow-2xl"
      />
    </div>

    <!-- Título -->
    <h1 class="text-5xl md:text-6xl font-extrabold mb-4 animate-slide-up">
      Olá, sou <span class="text-yellow-300">Ésley Nathan</span> 👋
    </h1>

    <!-- Subtitle -->
    <h2 class="text-2xl md:text-3xl font-semibold mb-6 text-primary-100">
      Desenvolvedor Full-Stack Python
    </h2>

    <!-- Descrição -->
    <p class="text-lg md:text-xl max-w-2xl mx-auto mb-10 text-primary-50 leading-relaxed">
      Construindo aplicações web escaláveis e modernas<br/>
      com Django, Angular e boas práticas de engenharia de software
    </p>

    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center mb-10">
      <a
        href="#projects"
        class="btn-primary bg-white text-primary-700 hover:bg-gray-100 px-8 py-4 text-lg font-semibold rounded-lg shadow-xl hover:scale-105 transition-transform duration-200"
      >
        Ver Projetos ↓
      </a>
      <a
        href="assets/cv/esley-nathan-cv.pdf"
        target="_blank"
        class="btn-secondary border-2 border-white text-white hover:bg-white hover:text-primary-700 px-8 py-4 text-lg font-semibold rounded-lg shadow-xl hover:scale-105 transition-transform duration-200"
      >
        Download CV 📄
      </a>
    </div>

    <!-- Social Links -->
    <div class="flex gap-6 justify-center text-3xl">
      <a href="https://github.com/esleynathan" target="_blank" rel="noopener noreferrer"
         class="hover:text-yellow-300 transition-colors duration-200">
        <i class="fab fa-github"></i>
      </a>
      <a href="https://linkedin.com/in/esleynathan" target="_blank" rel="noopener noreferrer"
         class="hover:text-yellow-300 transition-colors duration-200">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="mailto:seu-email@example.com"
         class="hover:text-yellow-300 transition-colors duration-200">
        <i class="fas fa-envelope"></i>
      </a>
    </div>
  </div>

  <!-- Scroll Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
    <i class="fas fa-chevron-down text-3xl text-white opacity-70"></i>
  </div>
</section>
```

### 2. About Section (Layout Duas Colunas)

```html
<section id="about" class="py-20 bg-white">
  <div class="container mx-auto px-4">
    <h2 class="text-4xl font-bold text-center text-gray-900 mb-12">
      Sobre Mim
    </h2>

    <div class="max-w-5xl mx-auto">
      <div class="flex flex-col md:flex-row gap-10 items-start">
        <!-- Foto -->
        <div class="flex-shrink-0 mx-auto md:mx-0">
          <img
            src="assets/images/profile-about.jpg"
            alt="Ésley Nathan - Desenvolvedor Full-Stack"
            class="w-64 h-64 md:w-72 md:h-72 rounded-lg object-cover shadow-2xl border-4 border-primary-100"
          />
        </div>

        <!-- Textos -->
        <div class="flex-1">
          <p class="text-lg text-gray-700 mb-4 leading-relaxed">
            Desenvolvedor Full-Stack Python com sólida experiência em construção de aplicações web escaláveis
            utilizando Django, Django REST Framework, Flask, Angular e React.
          </p>
          <p class="text-lg text-gray-700 mb-4 leading-relaxed">
            Engenheiro de Computação formado pela UniCarioca (2025) e cursando MBA em Engenharia de Software
            com IA na FullCycle. Atualmente atuando como Desenvolvedor Full Stack Python/Django na EDS
            (dentro do INEA - Instituto Estadual do Ambiente).
          </p>
          <p class="text-lg text-gray-700 mb-4 leading-relaxed">
            Experiência em desenvolvimento de APIs RESTful de alta performance, gerenciamento de bancos de dados
            PostgreSQL e Oracle, e trabalho em equipes ágeis (Scrum). Foco em código limpo, boas práticas de
            engenharia de software e documentação técnica detalhada.
          </p>
          <p class="text-lg text-gray-700 leading-relaxed">
            Busco continuamente aprimorar minhas habilidades técnicas e contribuir para projetos que gerem
            impacto real, aplicando os conhecimentos adquiridos em Python, Django, Angular/React, Docker e
            arquitetura de software moderna.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 3. Skills com Ícones e Proficiency

```html
<section id="skills" class="py-20 bg-gray-50">
  <div class="container mx-auto px-4">
    <h2 class="text-4xl font-bold text-center text-gray-900 mb-12">
      Habilidades Técnicas
    </h2>

    <!-- Frontend -->
    <div class="max-w-6xl mx-auto mb-12">
      <h3 class="text-2xl font-semibold text-gray-800 mb-6 flex items-center">
        <i class="fas fa-laptop-code text-primary-600 mr-3"></i>
        Frontend
      </h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        <!-- Angular -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3">
            <i class="fab fa-angular text-red-600"></i>
          </div>
          <h4 class="font-bold text-lg mb-2">Angular</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 90%"></div>
          </div>
        </div>

        <!-- React -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3">
            <i class="fab fa-react text-blue-400"></i>
          </div>
          <h4 class="font-bold text-lg mb-2">React</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 75%"></div>
          </div>
        </div>

        <!-- Adicionar mais skills... -->
      </div>
    </div>

    <!-- Backend -->
    <div class="max-w-6xl mx-auto mb-12">
      <h3 class="text-2xl font-semibold text-gray-800 mb-6 flex items-center">
        <i class="fas fa-server text-primary-600 mr-3"></i>
        Backend
      </h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        <!-- Python -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3">
            <i class="fab fa-python text-blue-500"></i>
          </div>
          <h4 class="font-bold text-lg mb-2">Python</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 95%"></div>
          </div>
        </div>

        <!-- Django -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3 text-green-700">
            <i class="fas fa-leaf"></i> <!-- Django icon placeholder -->
          </div>
          <h4 class="font-bold text-lg mb-2">Django</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 95%"></div>
          </div>
        </div>

        <!-- Adicionar mais skills... -->
      </div>
    </div>

    <!-- DevOps & Ferramentas -->
    <div class="max-w-6xl mx-auto">
      <h3 class="text-2xl font-semibold text-gray-800 mb-6 flex items-center">
        <i class="fas fa-tools text-primary-600 mr-3"></i>
        DevOps & Ferramentas
      </h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        <!-- Docker -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3">
            <i class="fab fa-docker text-blue-500"></i>
          </div>
          <h4 class="font-bold text-lg mb-2">Docker</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 80%"></div>
          </div>
        </div>

        <!-- Git -->
        <div class="card p-6 text-center hover:shadow-xl transition-shadow duration-200">
          <div class="text-5xl mb-3">
            <i class="fab fa-git-alt text-orange-600"></i>
          </div>
          <h4 class="font-bold text-lg mb-2">Git</h4>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div class="bg-primary-600 h-2 rounded-full" style="width: 90%"></div>
          </div>
        </div>

        <!-- Adicionar mais skills... -->
      </div>
    </div>
  </div>
</section>
```

### 4. Project Cards Modernos

```html
<div class="card group overflow-hidden hover:shadow-2xl transition-all duration-300 hover:-translate-y-1">
  <!-- Imagem do Projeto -->
  <div class="relative h-48 overflow-hidden bg-gray-200">
    <img
      *ngIf="project.image"
      [src]="project.image"
      [alt]="project.title"
      class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
    />
    <div *ngIf="!project.image"
         class="w-full h-full flex items-center justify-center text-gray-400 text-6xl">
      <i class="fas fa-code"></i>
    </div>

    <!-- Badge Featured -->
    <div *ngIf="project.featured"
         class="absolute top-4 right-4 bg-yellow-400 text-gray-900 px-3 py-1 rounded-full text-sm font-bold flex items-center gap-1">
      <i class="fas fa-star"></i> Destaque
    </div>
  </div>

  <!-- Conteúdo -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900 mb-2">{{ project.title }}</h3>
    <p class="text-gray-600 mb-4 line-clamp-3">{{ project.description }}</p>

    <!-- Tecnologias -->
    <div class="flex flex-wrap gap-2 mb-4">
      <span *ngFor="let tech of project.technologies.split(',')"
            class="text-xs bg-primary-100 text-primary-700 px-3 py-1 rounded-full font-medium">
        {{ tech.trim() }}
      </span>
    </div>

    <!-- Links -->
    <div class="flex gap-3">
      <a *ngIf="project.github_url"
         [href]="project.github_url"
         target="_blank"
         rel="noopener noreferrer"
         class="flex items-center gap-2 text-gray-700 hover:text-primary-600 transition-colors">
        <i class="fab fa-github"></i> GitHub
      </a>
      <a *ngIf="project.live_url"
         [href]="project.live_url"
         target="_blank"
         rel="noopener noreferrer"
         class="flex items-center gap-2 text-primary-600 hover:text-primary-700 font-semibold transition-colors">
        <i class="fas fa-external-link-alt"></i> Demo
      </a>
    </div>
  </div>
</div>
```

---

## ✨ Animações e Transições

### CSS Customizado (adicionar em styles.css)

```css
/* Animações de entrada */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Classes de utilidade */
.animate-fade-in {
  animation: fadeIn 1s ease-out;
}

.animate-slide-up {
  animation: slideUp 0.6s ease-out;
}

.animate-slide-in-left {
  animation: slideInLeft 0.6s ease-out;
}

/* Hover effects */
.hover-scale {
  transition: transform 0.3s ease;
}

.hover-scale:hover {
  transform: scale(1.05);
}

/* Gradients */
.gradient-text {
  background: linear-gradient(to right, #2563eb, #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## 📱 Responsividade

### Breakpoints Tailwind
- **sm**: 640px (tablets pequenos)
- **md**: 768px (tablets)
- **lg**: 1024px (desktops)
- **xl**: 1280px (desktops grandes)

### Padrão Mobile-First

```html
<!-- Exemplo: Hero Title -->
<h1 class="text-4xl sm:text-5xl md:text-6xl font-bold">
  Título Responsivo
</h1>

<!-- Exemplo: Grid Skills -->
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
  <!-- Cards -->
</div>

<!-- Exemplo: About Layout -->
<div class="flex flex-col md:flex-row gap-8">
  <!-- Mobile: stack vertical -->
  <!-- Desktop: layout horizontal -->
</div>
```

---

## 🔧 Ferramentas e Bibliotecas

### Font Awesome (Ícones)
```html
<!-- Adicionar no index.html -->
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
```

### Google Fonts (Opcional - melhorar tipografia)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
```

```css
/* No tailwind.config.js */
theme: {
  extend: {
    fontFamily: {
      sans: ['Inter', 'sans-serif'],
    }
  }
}
```

---

## ✅ Checklist de Implementação

### Preparação
- [ ] Criar pasta `frontend/src/assets/images/`
- [ ] Preparar fotos profissionais (perfil hero + about)
- [ ] Preparar screenshots dos projetos
- [ ] Adicionar Font Awesome CDN no index.html

### Hero Section
- [ ] Implementar novo layout com foto
- [ ] Adicionar gradient background
- [ ] Criar botões CTA (Ver Projetos + Download CV)
- [ ] Adicionar social links com ícones
- [ ] Implementar animações de entrada

### About Section
- [ ] Escolher layout (centralizado ou duas colunas)
- [ ] Adicionar foto profissional
- [ ] Ajustar textos existentes para nova estrutura

### Skills Section
- [ ] Adicionar ícones Font Awesome
- [ ] Implementar barras de proficiência
- [ ] Organizar por categorias
- [ ] Adicionar hover effects

### Projects Section
- [ ] Refatorar cards com imagens no topo
- [ ] Adicionar badge "Destaque" nos featured
- [ ] Implementar hover effects (scale + shadow)
- [ ] Adicionar links GitHub/Demo com ícones

### Navegação
- [ ] Implementar scroll spy (highlight seção atual)
- [ ] Adicionar botão "voltar ao topo"
- [ ] Testar smooth scroll

### Geral
- [ ] Adicionar transições suaves em todos os elementos
- [ ] Testar responsividade mobile/tablet/desktop
- [ ] Validar acessibilidade (alt texts, contrast)
- [ ] Performance check (Lighthouse)

---

## 📊 Métricas de Sucesso

- [ ] Lighthouse Score > 90 (Performance)
- [ ] Tempo de carregamento < 3s
- [ ] Design responsivo em todos os breakpoints
- [ ] Todos os CTAs funcionais
- [ ] Zero erros de console
- [ ] Acessibilidade WCAG AA

---

**Documento criado em**: 2025-12-05
**Versão**: 1.0
**Status**: Pronto para implementação
