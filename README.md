# Portfolio Ésley Nathan

> Uma aplicação web completa desenvolvida como portfólio técnico. O projeto demonstra habilidades em desenvolvimento desacoplado (Django/Angular), otimizações de performance, SEO, acessibilidade e uma arquitetura de documentação projetada para colaboração eficiente com assistentes de IA.

[![Status](https://img.shields.io/badge/status-MVP_4_Concluído-brightgreen)](./docs/STATUS.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Este repositório contém o código-fonte do meu portfólio pessoal, um projeto full-stack que serve como uma demonstração prática de engenharia de software moderna, aplicando conceitos do meu MBA em Engenharia de Software com IA.

## ✨ Principais Características

- **Arquitetura Desacoplada**: Backend API-first com Django REST Framework e Frontend SPA com Angular.
- **Containerização Completa**: Ambiente de desenvolvimento e produção 100% containerizado com Docker e Docker Compose.
- **Design Moderno e Responsivo**: Interface construída com Tailwind CSS, focada em UX e acessibilidade.
- **Documentação Orientada a IA**: Estrutura de documentação atômica (`STATUS`, `ARCHITECTURE`, `CONTRIBUTING`) para otimizar a colaboração com assistentes de código.

## 🚀 Quick Start (Docker)

### Pré-requisitos
- Docker e Docker Compose instalados
- Git

### Rodando o projeto
```bash
# 1. Clone o repositório
git clone https://github.com/esleynathan/meuportfolio.git
cd portfolio-esley

# 2. Inicie os containers em modo detached
docker-compose up -d --build

# 3. Acesse os serviços
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

Este projeto foi desenvolvido em um fluxo de trabalho moderno, onde a arquitetura e as decisões estratégicas são orquestradas pelo desenvolvedor, com a implementação acelerada por assistentes de IA.
