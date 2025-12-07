# Plano de Ação: MVP 5 - Deploy

**Última atualização**: 2024-05-22

Este documento detalha o passo a passo para a conclusão do **MVP 5**, que consiste em containerizar e publicar a aplicação em um ambiente de produção.

---

## 🎯 Objetivo

Publicar o portfólio online de forma segura, escalável e automatizada, utilizando Docker e um provedor de nuvem.

---

## ✅ Checklist de Tarefas

### Fase 1: Dockerização do Ambiente de Desenvolvimento

O objetivo desta fase é criar um ambiente de desenvolvimento consistente e isolado, que espelhe a estrutura de produção mas com ferramentas de agilidade como *hot-reloading*.

- [x] **1.1.** Criar `docker-compose.override.yml` para configurar os serviços de `backend` e `frontend` para desenvolvimento.
- [x] **1.2.** Atualizar `README.md` com as instruções para rodar o ambiente de desenvolvimento (`docker-compose up`).
- [x] **1.3.** Testar o ambiente de desenvolvimento localmente e confirmar o funcionamento do *hot-reloading* para frontend e backend.

### Fase 2: Dockerização do Ambiente de Produção

Nesta fase, criaremos os artefatos para construir imagens Docker otimizadas para produção.
- [x] **2.1.** Criar `backend/Dockerfile` para construir a imagem do Django com Gunicorn.
- [x] **2.2.** Criar `frontend/Dockerfile` (multi-stage) para compilar o Angular e preparar uma imagem final com Nginx.
- [x] **2.3.** Criar `frontend/nginx.conf` com as regras de reverse proxy para a API e o tratamento de rotas da SPA.
- [x] **2.4.** Criar o arquivo `.env.example` para gerenciar as variáveis de ambiente e garantir que `.env` está no `.gitignore`.

### Fase 3: Simulação do Ambiente de Produção Localmente

- [ ] **3.1.** Executar `docker-compose -f docker-compose.yml up --build` para testar a stack de produção na máquina local.
- [ ] **3.2.** Validar o acesso via `http://localhost` e confirmar que a comunicação entre Nginx e a API do backend está funcionando.

### Fase 4: Deploy em Nuvem

- [ ] **4.1.** Provisionar uma VM (Droplet/EC2) com Ubuntu.
- [ ] **4.2.** Instalar Docker e Docker Compose na VM.
- [ ] **4.3.** Clonar o repositório do projeto na VM.
- [ ] **4.4.** Criar o arquivo `.env` de produção na VM com as credenciais seguras (ex: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=esleynathan.com.br`).
- [ ] **4.5.** Executar `docker-compose -f docker-compose.yml up -d` para iniciar a aplicação em produção.

### Fase 5: Configuração Final e Go-Live

- [ ] **5.1.** Configurar o registro DNS do domínio para apontar para o IP da VM.
- [ ] **5.2.** Configurar SSL/HTTPS (Let's Encrypt com Certbot) para garantir a comunicação segura.
- [ ] **5.3.** Validar o acesso via `https://esleynathan.com.br` e realizar testes finais.