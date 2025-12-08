# Portfolio Ésley Nathan

> Aplicação web full-stack que serve como um portfólio técnico e uma demonstração prática de engenharia de software moderna. O projeto é totalmente containerizado e documentado seguindo uma arquitetura que otimiza a colaboração com assistentes de IA.

[![Status](https://img.shields.io/badge/status-MVP_5_Em_Andamento-blue)](./docs/STATUS.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

O projeto está atualmente na fase de **deploy (MVP 5)**, sendo containerizado com Docker para publicação em um ambiente de nuvem.

## ✨ Principais Características

- **Arquitetura Desacoplada**: Backend API-first com Django REST Framework e Frontend SPA com Angular.
- **Containerização Completa**: Ambiente de desenvolvimento e produção 100% containerizado com Docker e Docker Compose.
- **Design Moderno e Responsivo**: Interface construída com Tailwind CSS, focada em UX e acessibilidade.
- **Documentação Orientada a IA**: Estrutura de documentação atômica (`STATUS`, `ARCHITECTURE`, etc.) para otimizar a colaboração com assistentes de código.

## 🚀 Quick Start (Docker)
 
### Ambiente de Desenvolvimento (com Hot-Reload)
```bash
# 1. Clone o repositório
git clone https://github.com/esleynathan/portfolio-esley.git
cd portfolio-esley

# 2. Crie o arquivo .env a partir do exemplo
cp .env.example .env

# 3. Inicie os contêineres usando o perfil "dev"
docker-compose --profile dev up --build

# 4. Acesse os serviços
Frontend: http://localhost:4200 (com hot-reload)
Backend API: http://localhost:8000/api (com hot-reload)
```

### Ambiente de Produção (Simulado Localmente)
Para testar a build de produção exatamente como ela irá para a nuvem.
```bash
# Inicie os contêineres usando o perfil "prod"
docker-compose --profile prod up --build

# Acesse a aplicação
Frontend (Nginx): http://localhost
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
