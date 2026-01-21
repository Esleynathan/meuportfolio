# =============================================================================
# Portfolio - Backend + Frontend unificado
# =============================================================================
# Multi-stage build:
# 1. Compila o Angular
# 2. Prepara o Django com os arquivos estáticos do Angular
# =============================================================================

# Stage 1: Build do Frontend Angular
FROM node:20-alpine AS frontend-build

WORKDIR /frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ .

ENV NODE_OPTIONS="--max-old-space-size=1024"
RUN npm run build -- --configuration production

# Stage 2: Backend Python + Frontend compilado
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd dos2unix && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instala dependências Python
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia e prepara o entrypoint
COPY backend/entrypoint.sh /app/entrypoint.sh
RUN dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Copia o código do backend
COPY backend/ /app/

# Copia os arquivos compilados do Angular para o diretório do Django
COPY --from=frontend-build /frontend/dist/frontend/ /app/frontend/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
