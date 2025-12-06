# Portfolio Ésley Nathan

> Portfólio técnico demonstrando expertise em desenvolvimento full-stack, arquitetura de software e boas práticas de engenharia.

[![Status](https://img.shields.io/badge/status-MVP_1_completo-green)](./docs/STATUS.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

## Sobre o Projeto

Plataforma de portfólio desenvolvida para demonstrar competências em:

- Arquitetura moderna (API-first com Django REST)
- Frontend com Angular e Tailwind CSS
- Desenvolvimento multi-linguagem
- Containerização com Docker
- Sistemas concorrentes e escaláveis
- Boas práticas (Clean Code, SOLID, Design Patterns)

## Sobre

Desenvolvedor Full-Stack e Engenheiro de Computação focado em demonstrar capacidades técnicas através de projetos práticos e bem documentados.

## Stack Tecnológica

### Backend
- **Django REST Framework** - API RESTful
- **PostgreSQL** - Banco de dados
- **Python 3.11+**

### Frontend
- **Angular 17+** - Framework SPA
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **RxJS** - Programação reativa

### DevOps
- **Docker** - Containerização
- **Docker Compose** - Orquestração local
- **Git** - Controle de versão

## Estrutura do Projeto

```
portfolio-esley/
├── backend/              # Django REST API
│   ├── api/             # Apps Django
│   ├── config/          # Configurações
│   └── requirements.txt
├── frontend/            # Angular App
│   ├── src/
│   ├── angular.json
│   └── package.json
├── docs/                # Documentação
├── docker-compose.yml   # Orquestração
└── README.md
```

## Quick Start

### Pré-requisitos
- Docker e Docker Compose instalados
- Git

### Rodando o projeto

```bash
# Clone o repositório
git clone <seu-repositorio>
cd portfolio-esley

# Inicie com Docker Compose
docker-compose up -d

# Acesse
Frontend: http://localhost:4200
Backend API: http://localhost:8000/api
Django Admin: http://localhost:8000/admin
API Docs (Swagger): http://localhost:8000/api/docs/
```

### Desenvolvimento local (sem Docker)

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### Frontend
```bash
cd frontend
npm install
ng serve
```

## API REST

A API backend está totalmente funcional e documentada com Swagger/OpenAPI.

**Principais endpoints:**
- `GET/POST /api/projects/` - Gerenciar projetos
- `GET /api/projects/featured/` - Projetos em destaque
- `GET/POST /api/skills/` - Gerenciar skills
- `GET /api/skills/by-category/` - Filtrar skills
- `POST /api/contacts/` - Formulário de contato

**Documentação completa**: [docs/API.md](./docs/API.md)
**Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## Documentação

- 📋 [**STATUS.md**](./docs/STATUS.md) - Status atual, métricas e próximos passos
- 🗺️ [**ROADMAP.md**](./docs/ROADMAP.md) - Planejamento e histórico de desenvolvimento
- 🔌 [**API.md**](./docs/API.md) - Documentação completa da API REST

## Contato

- **LinkedIn**: [linkedin.com/in/esleynathan](https://linkedin.com/in/esleynathan)
- **GitHub**: [github.com/esleynathan](https://github.com/esleynathan)

## Licença

MIT License - Sinta-se livre para usar este projeto como referência.

---

**Desenvolvido com Claude Code** - Demonstrando uso de IA na engenharia de software moderna.
