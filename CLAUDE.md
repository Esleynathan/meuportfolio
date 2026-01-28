# Portfolio Ésley Nathan - Contexto do Projeto

## Visão Geral

Portfolio pessoal full-stack com Django REST API (backend) e Angular SPA (frontend).

- **Site**: https://esleynathan.com.br
- **Stack**: Django 5.2 + Angular 15 + PostgreSQL + Tailwind CSS
- **Deploy**: Docker + Traefik + GitHub Actions

---

## Estrutura do Projeto

```
portfolio-esley/
├── backend/                 # Django REST API
│   ├── config/              # Configurações Django (settings.py, urls.py)
│   ├── projects/            # App: Projetos do portfolio
│   ├── skills/              # App: Habilidades técnicas
│   └── contacts/            # App: Formulário de contato
├── frontend/                # Angular SPA
│   └── src/app/
│       ├── components/      # Componentes (navbar, hero, projects, skills, contact, footer)
│       ├── services/        # Serviços HTTP (projects, skills, contact)
│       └── models/          # Interfaces TypeScript
├── traefik/                 # Configuração do reverse proxy
├── infrastructure/          # Arquivos DevOps
├── docs/                    # Documentação detalhada
└── docker-compose.yml       # Orquestração Docker
```

---

## Backend (Django)

### Apps e Models

#### Projects (`backend/projects/models.py`)
```python
class Project:
    CATEGORY_CHOICES = [
        ('automation', 'Automação'),
        ('challenges', 'Desafios Técnicos'),
        ('applications', 'Aplicações'),
    ]

    title: CharField(200)
    slug: SlugField (auto-gerado)
    description: CharField(300)        # Resumo curto
    detailed_description: TextField    # Descrição completa
    image: ImageField (opcional)       # Upload para projects/
    technologies: CharField            # Separado por vírgula
    category: CharField(20)            # automation, challenges, applications
    github_url: URLField (opcional)
    live_url: URLField (opcional)
    featured: BooleanField             # Destaque na home
    order: IntegerField                # Ordem de exibição
    created_at, updated_at: DateTimeField
```

#### Skills (`backend/skills/models.py`)
```python
class Skill:
    name: CharField (único)
    category: CharField (choices)      # frontend, backend, database, devops, tools, other
    proficiency_level: CharField       # basic, intermediate, advanced, expert
    icon: ImageField (opcional)
    order: IntegerField
    created_at, updated_at: DateTimeField
```

#### Contacts (`backend/contacts/models.py`)
```python
class Contact:
    name: CharField(200)
    email: EmailField
    subject: CharField(300)
    message: TextField
    read: BooleanField
    created_at: DateTimeField
```

### Endpoints da API

| Método | Endpoint | Descrição | Permissão |
|--------|----------|-----------|-----------|
| GET | `/api/projects/` | Lista projetos | Público |
| GET | `/api/projects/?category=automation` | Filtra por categoria | Público |
| GET | `/api/projects/featured/` | Projetos em destaque | Público |
| GET | `/api/projects/{id}/` | Detalhes do projeto | Público |
| POST | `/api/projects/` | Criar projeto | Admin |
| GET | `/api/skills/` | Lista skills (paginado) | Público |
| GET | `/api/skills/?category=frontend` | Skills por categoria | Público |
| POST | `/api/contacts/` | Enviar mensagem | Público |
| GET | `/api/contacts/` | Listar mensagens | Admin |

### URLs Importantes

- `/x/` - Django Admin (renomeado de /admin)
- `/api/docs/` - Swagger UI
- `/api/schema/` - OpenAPI Schema

---

## Frontend (Angular)

### Componentes Principais

| Componente | Arquivo | Função |
|------------|---------|--------|
| NavbarComponent | `components/navbar/` | Navegação + dark mode toggle |
| HeroComponent | `components/hero/` | Seção inicial |
| AboutComponent | `components/about/` | Sobre mim |
| ProjectsComponent | `components/projects/` | Projetos agrupados por categoria |
| SkillsComponent | `components/skills/` | Skills por categoria |
| ContactComponent | `components/contact/` | Formulário de contato |
| FooterComponent | `components/footer/` | Rodapé |

### Services

| Service | Métodos |
|---------|---------|
| ProjectsService | `getProjects()`, `getFeaturedProjects()`, `getProjectById(id)` |
| SkillsService | `getSkills()`, `getSkillsByCategory(category)` |
| ContactService | `sendMessage(data)` |

### Models (TypeScript)

```typescript
// models/project.model.ts
interface Project {
  id: number;
  title: string;
  slug: string;
  description: string;
  detailed_description: string;
  technologies: string;
  category: string;              // 'automation' | 'challenges' | 'applications'
  category_display?: string;     // Label legível (ex: "Automação")
  github_url: string;
  live_url?: string;
  image?: string;
  featured: boolean;
  order: number;
}

// models/skill.model.ts
interface Skill {
  id: number;
  name: string;
  category: string;
  proficiency_level: number;
  icon?: string;
  order: number;
}
```

### Estilização

- **Framework**: Tailwind CSS (utility-first)
- **Dark Mode**: Classe `dark` no `<html>` (padrão ativo)
- **Config**: `frontend/tailwind.config.js`
- **Cores customizadas**: `primary` (sky blue palette)
- **Fontes**: Inter (sans), Fira Code (mono)

---

## Comandos

### Desenvolvimento Local

```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver     # http://localhost:8000

# Frontend
cd frontend
npm install
ng serve                       # http://localhost:4200
```

### Docker (Desenvolvimento)

```bash
docker compose --profile dev up --build

# Acesso:
# Frontend: http://localhost:4200
# Backend:  http://localhost:8000
```

### Docker (Produção)

```bash
docker compose up -d --build
```

### Testes

```bash
# Backend
python manage.py test

# Frontend
npm test
```

### Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar Superuser

```bash
python manage.py createsuperuser
```

---

## Configurações Importantes

### Backend (`config/settings.py`)

- **LANGUAGE_CODE**: `pt-br`
- **TIME_ZONE**: `America/Sao_Paulo`
- **Paginação**: 10 items por página
- **CORS**: Configurado para localhost:4200 e esleynathan.com.br
- **Static files**: WhiteNoise (serve Angular build)

### Frontend (`angular.json`)

- **Build output**: `dist/frontend/`
- **Environment files**: `src/environments/`
- **Proxy dev**: `proxy.conf.json` (API para localhost:8000)

---

## Variáveis de Ambiente (.env)

```bash
# Database
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=<senha>

# Django
SECRET_KEY=<chave>
DEBUG=False
ALLOWED_HOSTS=esleynathan.com.br,www.esleynathan.com.br

# Security (produção)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## Padrões do Projeto

### Convenções de Código

- **Backend**: snake_case (Python/Django)
- **Frontend**: camelCase (TypeScript/Angular)
- **CSS**: Tailwind utilities direto no template
- **Commits**: Conventional Commits (`feat:`, `fix:`, `docs:`)

### Fluxo de Dados

1. Angular Service faz request HTTP
2. Django ViewSet processa e retorna JSON
3. Service transforma resposta (ex: extrai `results` de paginação)
4. Component recebe Observable e renderiza

### Paginação (Frontend)

O SkillsService usa RxJS `expand()` + `reduce()` para buscar todas as páginas automaticamente.

---

## Arquivos Críticos

### Backend
- `backend/config/settings.py` - Configurações Django
- `backend/config/urls.py` - Rotas da API
- `backend/projects/models.py` - Model de Project
- `backend/projects/serializers.py` - Serializer de Project
- `backend/projects/views.py` - ViewSet de Project

### Frontend
- `frontend/src/app/app.module.ts` - Módulo principal
- `frontend/src/app/components/projects/` - Componente de projetos
- `frontend/src/app/services/projects.service.ts` - Service de projetos
- `frontend/src/environments/environment.ts` - Config de ambiente

### DevOps
- `docker-compose.yml` - Orquestração
- `Dockerfile` - Build multi-stage
- `.github/workflows/deploy.yml` - CI/CD
