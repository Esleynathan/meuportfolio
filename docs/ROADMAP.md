# Roadmap - Portfolio Ésley Nathan

Planejamento e acompanhamento do desenvolvimento do portfólio técnico.

**Última atualização**: 2024-05-22
**Status**: MVP 4 COMPLETO ✅ | Próximo: MVP 5

---

## Estratégia de MVPs

### ✅ MVP 1 - Landing Page Visual (COMPLETO)
**Objetivo**: Interface visual funcional e responsiva

**Entregas**:
- [x] Django REST API com 3 models (Project, Skill, Contact)
- [x] 15+ endpoints REST documentados
- [x] Swagger/OpenAPI configurado
- [x] Angular 17 com Tailwind CSS
- [x] 7 componentes criados (Navbar, Hero, About, Skills, Projects, Contact, Footer)
- [x] Design responsivo (mobile + desktop)
- [x] Menu hamburger mobile funcional

**Resultado**: Landing page visualmente completa, mas com dados mockados.

---

### ✅ MVP 2 - Integração Backend ↔ Frontend (COMPLETO)
**Objetivo**: Conectar frontend com API Django

**Entregas**:
- [x] Criar services Angular (projects.service, skills.service, contact.service)
- [x] Configurar HttpClient e environment
- [x] Conectar componentes à API real
- [x] Implementar formulário de contato funcional
- [x] Loading states e tratamento de erros
- [x] Validações no frontend
- [x] Tratamento de paginação do DRF (PaginatedResponse)

**Resultado**: Frontend totalmente integrado com backend, dados carregando dinamicamente da API.

---

### ⏳ MVP 3 - Conteúdo Real + UX Moderno (EM ANDAMENTO)
**Objetivo**: Adicionar conteúdo real e implementar melhorias UX/Design modernas

#### Fase 3A - Conteúdo Real (PENDENTE)
**Entregas planejadas**:
- [x] Adicionar 3-5 projetos reais via Django Admin
  - Títulos, descrições detalhadas, tecnologias
  - URLs do GitHub e demo (se aplicável)
  - Imagens/screenshots dos projetos
  - Marcar projetos featured
- [x] Adicionar todas as skills reais via Django Admin
  - Categorizar: Frontend, Backend, DevOps, Ferramentas
  - Definir níveis de proficiência (1-5)
  - URLs dos ícones (DevIcon CDN)
  - Ordenar por relevância
- [x] Customizar textos "Sobre Mim" ✅ (dados reais do CV)
- [x] Adicionar foto profissional ✅ (profile.jpg em assets/images/)
- [x] Links para GitHub e LinkedIn funcionais ✅ (Hero Section com target="_blank")

**Status**: Infraestrutura pronta, aguardando curadoria manual de conteúdo via Django Admin.

#### Fase 3B - Melhorias UX/Design Modernas ⏳ (EM ANDAMENTO)
**Objetivo**: Implementar visual moderno e refinamentos de interface.

**1. Hero Section Aprimorado** ✅
- [x] Título principal impactante com destaque gradiente no nome e animação de aceno.
- [x] Subtitle descritivo "Desenvolvedor Full-Stack Python"
- [x] Dois CTAs principais:
  - [x] Botão primário: "Ver Projetos ↓" (scroll suave para #projects)
  - [x] Botão secundário: "Download CV 📄" (download de PDF)
- [x] Background gradient animado (from-primary-600 via-primary-700 to-purple-800)
- [x] Efeitos decorativos com blur e animate-pulse
- [x] Social links com ícones, incluindo WhatsApp para contato direto.

**2. About Section Layout em Duas Colunas** ✅
- [x] Desktop: Foto à esquerda + texto à direita (flex-row)
- [x] Mobile: Stack vertical (flex-col)
- [x] Foto: w-64 h-64 md:w-72 md:h-72 rounded-lg shadow-2xl border-4
- [x] Animação slideInLeft na foto
- [x] Textos reais do CV mantidos

**3. Skills com Ícones e Proficiency** ✅
- [x] Exibição de ícones via campo `skill.icon` da API
- [x] Fallback para ícone Font Awesome (fa-code) quando sem imagem
- [x] Barra de proficiência visual com gradiente (from-primary-600 to-purple-600)
- [x] Cálculo dinâmico: `(proficiency_level / 5) * 100%`
- [x] Grid responsivo: 1 → 2 → 3 colunas
- [x] Hover effects: shadow-xl + scale-105
- [x] Exibição de categoria e descrição
- [x] Método handleImageError() para URLs quebradas

**4. Projects Cards Modernos** ✅
- [x] Cards com imagem de preview no topo (h-48)
- [x] Fallback com ícone fa-laptop-code para projetos sem imagem
- [x] Hover effects: shadow-2xl + scale-105 no card
- [x] Zoom na imagem ao hover (group-hover:scale-110)
- [x] Badges de tecnologias estilizados (rounded-full com border)
- [x] Links com ícones Font Awesome (fa-github, fa-external-link-alt)
- [x] Badge "⭐ Destaque" para projetos featured (gradient amarelo-laranja)
- [x] Truncamento de descrição com line-clamp-3
- [x] Plugin @tailwindcss/line-clamp instalado

**5. Navegação e Interações** ✅
- [x] Smooth scroll funcionando (CSS: scroll-behavior: smooth)
- [x] Botão "voltar ao topo" refinado para ser mais discreto (opacidade reduzida).
- [x] Rodapé modernizado com layout limpo, responsivo e centralizado.
- [x] Seção de Contato com largura ajustada para melhor UX em telas maiores.
- [ ] `feat(theme)`: Implementar Dark Mode.
- [x] `feat(navbar)`: Implementar Navbar Inteligente com Headroom.js.
- [ ] `fix(layout)`: Corrigir Cores de Fundo das Seções.
- [ ] `fix(layout)`: Corrigir Cores de Fundo das Seções. ⏳ **(EM ANDAMENTO)**
- [ ] `feat(theme)`: Implementar Dark Mode. ⏳ **(EM ANDAMENTO)**

**Estimativa total MVP 3**: 3-4 horas
- Fase 3A (Conteúdo): 1-1.5h
- Fase 3B (UX/Design): 2-2.5h

---

### 📅 MVP 4 - Polimento e Otimização
**Objetivo**: Refinamentos finais e otimizações de performance

**Entregas planejadas**:
- [ ] **Performance**
  - Lazy loading de imagens
  - Minificação de assets
  - Otimização de bundle size
  - Lighthouse score > 90
- [ ] **Acessibilidade (A11y)**
  - ARIA labels onde necessário
  - Contrast ratio adequado (WCAG AA)
  - Navegação por teclado
  - Alt texts em todas as imagens
- [ ] **SEO**
  - Meta tags (title, description, OG tags)
  - Schema.org markup (Person, WebSite)
  - Sitemap.xml
  - robots.txt
- [ ] **Analytics (Opcional)**
  - Google Analytics ou alternativa
  - Event tracking em CTAs
- [ ] **PWA (Opcional)**
  - Service Worker
  - Manifest.json
  - Offline fallback

---

### 📅 MVP 5 - Deploy
**Objetivo**: Publicar online

**Entregas planejadas**:
- [ ] Dockerização completa (backend + frontend + db)
- [ ] Deploy em VM (AWS, Azure ou DigitalOcean)
- [ ] Configurar Nginx como reverse proxy
- [ ] Domínio configurado
- [ ] SSL/HTTPS (Let's Encrypt)
- [ ] Monitoramento básico

---

## Projetos Demonstrativos (Futuro)

Após MVP 5, desenvolver projetos adicionais para portfolio:

### Python (3 projetos)
- Projeto Django #1
- Projeto Django #2
- Projeto Flask/FastAPI

### JavaScript/TypeScript (3 projetos)
- Projeto Angular
- Projeto React
- Projeto Node.js (backend/API)

Cada projeto será dockerizado e integrado à landing page.

---

## Decisões Técnicas Importantes

### Por que MVPs incrementais?
- ✅ Validação rápida de cada etapa
- ✅ Entregas tangíveis e testáveis
- ✅ Facilita ajustes de rota
- ✅ Evita over-engineering

### Por que Django REST + Angular + Tailwind?

**Django REST Framework**:
- Admin interface pronto para usar
- ORM poderoso e seguro
- Swagger integrado (drf-spectacular)
- Excelente documentação

**Angular 17**:
- Framework completo (não precisa bibliotecas extras)
- TypeScript nativo
- RxJS para programação reativa
- Arquitetura escalável para SPAs corporativas

**Tailwind CSS**:
- Zero dependências extras de UI
- CSS puro compilado (leve e performático)
- Totalmente customizável
- Responsivo por padrão
- Utilities-first approach

### Por que API-First?
- Backend e frontend completamente desacoplados
- Facilita manutenção independente
- Permite múltiplos frontends no futuro
- API reutilizável para outros projetos

---

## Histórico de Desenvolvimento

### Sessão 1 (2025-12-04) - Planejamento Inicial
**Decisões tomadas**:
- Definido stack: Django REST + Angular + Tailwind
- Estrutura de documentação minimalista (apenas essencial)
- Foco em entregar valor incremental
- Documentação detalhada criada conforme implementação

---

### Sessão 2 (2025-12-04) - Setup Inicial
**Entregas**:
- ✅ Fase 1.1 completa: Setup inicial finalizado
- Criado .gitignore com padrões Python, Node, Angular e Docker
- Criado docker-compose.yml com 3 serviços (db, backend, frontend)

**Decisão importante**: Desenvolver localmente primeiro, depois dockerizar completamente

---

### Sessão 3 (2025-12-04) - Backend Django Inicial
**Entregas**:
- ✅ Ambiente Python configurado (venv criado em backend/)
- ✅ Dependências instaladas: Django, DRF, psycopg2-binary, python-decouple, django-cors-headers, pillow, drf-spectacular
- ✅ requirements.txt gerado com todas as dependências
- ✅ Projeto Django inicializado (pasta config/ criada)
- ✅ Servidor de desenvolvimento testado e funcionando (http://127.0.0.1:8000)
- ✅ Arquivos .env e .env.example criados
- ✅ Django REST Framework configurado no settings.py
- ✅ CORS configurado para permitir requisições do Angular (localhost:4200)
- ✅ Configuração de variáveis de ambiente com python-decouple
- ✅ Swagger/OpenAPI configurado (drf-spectacular)
- ✅ Idioma PT-BR e timezone America/Sao_Paulo
- ✅ 3 apps Django criados: projects, skills, contacts
- ✅ Model Project criado com 13 campos (title, slug, description, image, technologies, etc.)
- ✅ Model Skill criado com 7 campos (name, category, proficiency_level, icon, order, etc.)
- ✅ Model Contact criado com 6 campos (name, email, subject, message, read, created_at)
- ✅ Migrations executadas: tabelas criadas no banco SQLite
- ✅ Banco de dados: projects_project, skills_skill, contacts_contact

**Estrutura criada**: backend/venv/, config/, manage.py, requirements.txt, .env, .env.example, db.sqlite3

**Decisão importante**: Pastas services/ e shared/ criadas para organização futura (Clean Architecture)

---

### Sessão 4 (2025-12-04) - API REST Completa
**Entregas**:
- ✅ Serializers criados para todos os models (ProjectSerializer, SkillSerializer, ContactSerializer)
- ✅ ViewSets criados com endpoints customizados:
  - ProjectViewSet com endpoint `/featured/`
  - SkillViewSet com endpoint `/by-category/`
  - ContactViewSet (apenas GET e POST públicos)
- ✅ URLs configuradas para cada app (projects/urls.py, skills/urls.py, contacts/urls.py)
- ✅ URLs principais configuradas (config/urls.py)
- ✅ Testes iniciais realizados: GET retornou lista vazia (esperado)

**Endpoints disponíveis**:
- GET/POST/PUT/DELETE /api/projects/
- GET /api/projects/featured/
- GET/POST/PUT/DELETE /api/skills/
- GET /api/skills/by-category/?category=Frontend
- GET/POST /api/contacts/ (apenas leitura e criação)
- GET /api/docs/ (Swagger UI)
- GET /api/schema/ (OpenAPI schema)

**Dados de teste**:
- ✅ Django Admin configurado para todos os models
- ✅ Superusuário criado
- ✅ Dados de teste adicionados via Admin
- ✅ API testada com dados reais (funcionando corretamente)

---

### Sessão 5 (2025-12-04) - Frontend Angular Completo
**Entregas**:
- ✅ Projeto Angular inicializado (ng new frontend --routing --style=css)
- ✅ Tailwind CSS instalado e configurado
- ✅ Paleta de cores personalizada criada (tons de azul para primary)
- ✅ Classes utilitárias criadas (.btn-primary, .btn-secondary, .card)
- ✅ Smooth scroll configurado
- ✅ 7 componentes criados:
  - navbar/ - Menu responsivo com hamburger mobile
  - hero/ - Seção de apresentação
  - about/ - Sobre mim
  - skills/ - Grid de habilidades
  - projects/ - Grid de projetos
  - contact/ - Formulário de contato
  - footer/ - Rodapé
- ✅ Template de teste validado (Tailwind CSS funcionando)
- ✅ ng serve testado e funcionando

**Decisões técnicas**:
- Escolhido tons de azul para cores primary (profissionalismo e confiança)
- Menu mobile com toggle state (Angular + Tailwind, zero dependências)
- Responsividade mobile-first (breakpoints: sm:, md:, lg:, xl:)
- Dados mockados nos componentes (integração com API no MVP 2)

**Estrutura criada**:
- frontend/src/app/components/ (7 componentes)
- frontend/tailwind.config.js (paleta customizada)
- frontend/src/styles.css (Tailwind imports + utilities)

**Resultado**: ✅ **MVP 1 COMPLETO** - Landing page visualmente funcional e responsiva

---

### Sessão 6 (2025-12-04) - Reorganização da Documentação
**Objetivo**: Limpar redundâncias e melhorar eficiência da documentação

**Entregas**:
- ✅ Criado docs/API.md com documentação completa da API REST
  - Todos os endpoints documentados
  - Exemplos de requisições (curl)
  - Schemas de objetos (JSON)
  - Códigos de erro
  - Autenticação
- ✅ README.md reduzido de 272 para 133 linhas (-51%)
  - Removidos detalhes da API (movidos para API.md)
  - Removidos exemplos de curl
  - Simplificada seção "Sobre Mim"
  - Mantido apenas Quick Start e estrutura essencial
- ✅ ROADMAP.md alinhado com estratégia de MVPs
  - Removidas fases antigas (2-6)
  - Adicionada estrutura de MVP 1-5
  - Histórico completo de sessões mantido
  - Decisões técnicas documentadas
- ✅ STATUS.md atualizado com referência ao API.md

**Separação de concerns**:
- **README.md**: Visão geral, Quick Start, Stack
- **STATUS.md**: Estado atual, métricas, próximos passos
- **ROADMAP.md**: Planejamento, história, decisões técnicas
- **API.md**: Documentação técnica completa da API

---

### Sessão 7 (2025-12-05) - Integração Backend ↔ Frontend
**Objetivo**: Implementar MVP 2 completo - conectar Angular com Django API

**Entregas**:
- ✅ **Environment Configuration**
  - Criado `environment.ts` com apiUrl: 'http://localhost:8000/api'
  - Criado `environment.prod.ts` para futuro deploy

- ✅ **TypeScript Models**
  - Criado `models/project.model.ts` (interface Project)
  - Criado `models/skill.model.ts` (interface Skill)
  - Criado `models/contact.model.ts` (interfaces ContactMessage e ContactResponse)

- ✅ **Angular Services**
  - Criado `services/projects.service.ts`:
    - `getProjects()`, `getFeaturedProjects()`, `getProjectById()`
    - Implementado `PaginatedResponse<T>` interface
    - Usado RxJS `map` operator para extrair `results` array
  - Criado `services/skills.service.ts`:
    - `getSkills()`, `getSkillsByCategory()`, `getSkillById()`
    - Mesmo tratamento de paginação
  - Criado `services/contact.service.ts`:
    - `sendMessage()` com POST para API

- ✅ **HttpClient Configuration**
  - Adicionado `HttpClientModule` no app.module.ts
  - Adicionado `ReactiveFormsModule` para formulários

- ✅ **Components Integration**
  - Atualizado `ProjectsComponent`:
    - Injeção de ProjectsService
    - Loading state (`isLoading`)
    - Error handling com retry button
    - Dados dinâmicos da API
  - Atualizado `SkillsComponent`:
    - Mesmo padrão de ProjectsComponent
    - Carregamento dinâmico de skills
  - Atualizado `ContactComponent`:
    - Reactive Forms com FormBuilder
    - Validações (required, minLength, email)
    - Helper methods (`isFieldInvalid`, `getFieldError`)
    - Submit com loading state
    - Mensagens de sucesso/erro

- ✅ **Bug Fix - Paginação DRF**
  - **Problema**: Angular error "NG02200: Cannot find a differ supporting object"
  - **Causa**: DRF retorna `{count, next, previous, results}`, não array direto
  - **Solução**:
    - Criado `interface PaginatedResponse<T>`
    - Usado RxJS `map(response => response.results)`
    - Pattern aplicado em ProjectsService e SkillsService
  - **Resultado**: Projetos e skills carregando corretamente

- ✅ **Content Update - About Section**
  - Substituído conteúdo mockado por dados reais do CV
  - Informações profissionais atualizadas:
    - Desenvolvedor Full-Stack Python
    - Engenheiro de Computação (UniCarioca 2025)
    - MBA Engenharia de Software com IA (FullCycle)
    - Atuação na EDS/INEA
    - Stack: Django, DRF, Flask, Angular, React, PostgreSQL, Oracle

**Decisões técnicas**:
1. **Generic Pagination Handling**: Criar `PaginatedResponse<T>` interface reutilizável em vez de tratar caso a caso
2. **Service Layer Pattern**: Manter componentes desacoplados da API, toda comunicação via services
3. **Reactive Forms**: Usar FormBuilder para código mais limpo e manutenível
4. **Loading States**: Implementar feedback visual para melhor UX
5. **Error Handling**: Mensagens user-friendly + console.error para debug

**Lições aprendidas**:
- Django REST Framework usa paginação por padrão
- RxJS `map` operator é essencial para transformar responses
- Reactive Forms helper methods melhoram muito a DX
- Separação de modelos/services/components facilita manutenção

**Resultado**: ✅ **MVP 2 COMPLETO** - Frontend totalmente integrado com backend

---

### Sessão 8 (2025-12-05) - MVP 3 Fase 3B - Melhorias UX/Design Modernas
**Objetivo**: Implementar visual moderno seguindo tendências 2025

**Entregas**:
- ✅ **Font Awesome 6 Integration**
  - Adicionado CDN no index.html
  - Biblioteca de ícones disponível globalmente

- ✅ **Assets Structure**
  - Criada pasta `frontend/src/assets/images/`
  - Foto profissional adicionada (profile.jpg)

- ✅ **Hero Section Redesign**
  - Background gradient animado (from-primary-600 via-primary-700 to-purple-800)
  - Efeitos decorativos com blur e animate-pulse
  - Foto de perfil circular (w-48 h-48 md:w-56 md:h-56)
  - Título impactante com nome destacado em amarelo
  - Subtitle "Desenvolvedor Full-Stack Python"
  - 2 CTAs principais:
    - "Ver Projetos ↓" - scroll suave para #projects
    - "Download CV 📄" - link para PDF
  - Social links com ícones (GitHub, LinkedIn, Email)
  - Scroll indicator animado (chevron-down com bounce)

- ✅ **About Section Two-Column Layout**
  - Desktop: foto à esquerda + texto à direita (flex-row)
  - Mobile: stack vertical (flex-col)
  - Foto com shadow-2xl e border-4 border-primary-100
  - Animação slideInLeft na foto
  - Textos reais do CV mantidos

- ✅ **Skills Component Modernization**
  - Exibição de ícones via `skill.icon` da API
  - Fallback para ícone Font Awesome (fa-code)
  - Barra de proficiência visual com gradiente
  - Cálculo dinâmico: `(proficiency_level / 5) * 100%`
  - Grid responsivo: 1 → 2 → 3 colunas
  - Hover effects: shadow-xl + scale-105
  - Exibição de categoria e descrição
  - Método `handleImageError()` para URLs quebradas

- ✅ **Projects Component Modernization**
  - Cards com imagem de preview (h-48)
  - Fallback com ícone fa-laptop-code
  - Hover effects: shadow-2xl + scale-105
  - Zoom na imagem ao hover (group-hover:scale-110)
  - Badges de tecnologias estilizados (rounded-full com border)
  - Links com ícones Font Awesome
  - Badge "⭐ Destaque" para projetos featured
  - Truncamento de descrição com line-clamp-3
  - Plugin @tailwindcss/line-clamp instalado

- ✅ **Custom CSS Animations**
  - Keyframes criados: fadeIn, slideUp, slideInLeft
  - Aplicados no Hero (foto, título) e About (foto)
  - Durations: 0.6s a 1s ease-out

- ✅ **Back to Top Button**
  - Fixed position bottom-8 right-8
  - Aparece após scroll > 300px
  - Smooth scroll ao topo
  - Hover: scale-110 + bounce no ícone
  - @HostListener('window:scroll') no app.component.ts

**Decisões técnicas**:
1. **Tailwind-only approach**: Sem bibliotecas de componentes, apenas Tailwind + Font Awesome
2. **Performance**: Animações CSS puras (não JavaScript)
3. **Responsividade**: Mobile-first com breakpoints Tailwind
4. **Acessibilidade**: aria-label em botões, alt text em imagens
5. **Error handling**: Método handleImageError() em Skills e Projects

**Arquivos modificados**:
- `frontend/src/index.html` - Font Awesome CDN
- `frontend/src/app/components/hero/hero.component.html` - Redesign completo
- `frontend/src/app/components/about/about.component.html` - Layout duas colunas
- `frontend/src/app/components/skills/skills.component.html` - Ícones + proficiência
- `frontend/src/app/components/skills/skills.component.ts` - handleImageError()
- `frontend/src/app/components/projects/projects.component.html` - Cards modernos
- `frontend/src/app/components/projects/projects.component.ts` - handleImageError()
- `frontend/src/app/app.component.html` - Botão back to top
- `frontend/src/app/app.component.ts` - Lógica scroll tracking
- `frontend/src/styles.css` - Animações CSS customizadas
- `frontend/tailwind.config.js` - Plugin line-clamp

**Resultado**: ✅ **MVP 3 FASE 3B COMPLETO** - UX/Design moderno implementado, aguardando apenas curadoria de conteúdo

---

### Sessão 9 (2025-12-07) - MVP 5 Fase 1 - Dockerização do Ambiente de Desenvolvimento
**Objetivo**: Corrigir e estabilizar o ambiente de desenvolvimento com Docker.

**Entregas**:
- ✅ **Correção do Backend**:
  - **Problema**: Comando `wait_for_db` não encontrado.
  - **Causa**: Arquivo `wait_for_db.py` estava em múltiplos locais incorretos.
  - **Solução**: Manter apenas a cópia em `backend/config/management/commands/wait_for_db.py` e remover as duplicatas.

- ✅ **Correção do Frontend**:
  - **Problema**: Contêiner `portfolio-frontend-dev` falhava ao iniciar com erro `ng: not found`.
  - **Causa**: O `Dockerfile` de produção do frontend não instalava as dependências de desenvolvimento (`@angular/cli`). O volume anônimo para `node_modules` também sobrescrevia a pasta.
  - **Solução**:
    - Criado `frontend/Dockerfile.dev` específico para o ambiente de desenvolvimento, que executa `npm install`.
    - Atualizado `docker-compose.override.yml` para usar o novo `Dockerfile.dev` no serviço `frontend`.
    - Alterado o volume de `node_modules` para um volume nomeado (`frontend_node_modules`), garantindo a persistência das dependências entre as execuções.

- ✅ **Documentação da Arquitetura**:
  - Atualizado `docs/ARCHITECTURE.md` com uma seção detalhada sobre os ambientes Docker de desenvolvimento e produção, explicando os contêineres e Dockerfiles utilizados em cada um.

**Resultado**: ✅ **Ambiente de desenvolvimento Docker 100% funcional** com hot-reloading para backend e frontend.
---

### Sessão 10 (2025-12-07) - MVP 5 Fase 2 - Preparação do Ambiente de Produção
**Objetivo**: Garantir que o ambiente de produção sirva todos os arquivos estáticos corretamente.

**Entregas**:
- ✅ **Configuração de Arquivos Estáticos do Django**:
  - **Problema**: O Django com `DEBUG=False` não serve seus próprios arquivos estáticos (CSS/JS do Admin).
  - **Solução**:
    - [x] Adicionado `STATIC_ROOT` no `settings.py`.
    - [x] Adicionado o comando `collectstatic` ao `backend/entrypoint.sh`.
    - [x] Criado um volume nomeado `static_data` no `docker-compose.yml` para compartilhar os arquivos estáticos entre o `backend` e o `nginx`.
    - [x] Adicionada uma nova rota `location /static/` no `frontend/nginx.conf` para que o Nginx sirva os arquivos coletados.

**Resultado**: ✅ **Ambiente de produção pronto para ser testado**, com o Nginx configurado para servir tanto a aplicação Angular quanto os arquivos estáticos do Django Admin.
---

### Sessão 11 (2025-12-09) - MVP 5 Fase 3 - Fortalecimento de Segurança (Hardening)
**Objetivo**: Proteger a aplicação contra acessos não autorizados e ataques automatizados.

**Entregas**:
- ✅ **Proteção da API (Endpoints de Escrita)**:
  - **Problema**: Endpoints de `POST`, `PUT`, `DELETE` estavam abertos, permitindo que qualquer um modificasse os dados.
  - **Solução**: Implementado `permission_classes` em todas as `ViewSets` (`Project`, `Skill`, `Contact`).
    - Ações de leitura (`GET`) permanecem públicas.
    - Ações de escrita (`POST`, `PUT`, `DELETE`) agora exigem autenticação de administrador (`IsAdminUser`).
    - A `ContactViewSet` permite `POST` público, mas a leitura (`GET`) é restrita a administradores.

- ✅ **Proteção do Django Admin**:
  - **Problema**: A URL `/admin/` é um alvo comum para ataques de força bruta.
  - **Solução**: A URL do admin foi alterada para um caminho não-padrão (`/x/`).
    - Atualizado `backend/config/urls.py` para registrar a nova rota.
    - Atualizado `frontend/nginx.conf` para criar o proxy reverso para a nova rota.

**Resultado**: ✅ **Aplicação significativamente mais segura**. Acesso de escrita à API e ao painel administrativo agora estão devidamente restritos a usuários autorizados.
---

## Métricas de Sucesso

| Métrica | Status | Observação |
|---------|--------|------------|
| Landing page responsiva | ✅ | Mobile + Desktop |
| API REST documentada | ✅ | Swagger + docs/API.md |
| Frontend funcional | ✅ | Integração completa |
| Dados reais | ⏳ | MVP 3 (About completo, falta projetos/skills) |
| Deploy online | ❌ | MVP 5 |

---

## Riscos e Mitigações

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Escopo crescer demais | Alto | Manter foco estrito nos MVPs |
| Complexidade do Docker | Médio | Começar simples, um container por vez |
| Deploy em VM pode falhar | Médio | Testar localmente primeiro, documentar processo |
| Tempo de aprendizado | Baixo | Usando tecnologias já conhecidas |

---

## Próximas Decisões Necessárias

- Nome de domínio (para MVP 5)
- Provider de VM: AWS, Azure ou DigitalOcean (para MVP 5)
- Estratégia de backup (para MVP 5)
- Ferramenta de monitoramento (para MVP 5)

---

**Lembre-se**: Projeto de longo prazo. Melhor entregar incrementalmente do que tentar fazer tudo de uma vez.

**Próximo passo**: Iniciar MVP 3 - Adicionar conteúdo real (projetos e skills via Django Admin).
