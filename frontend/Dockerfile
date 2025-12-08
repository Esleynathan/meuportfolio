# Stage 1: Build - Compila a aplicação Angular
FROM node:20-alpine AS build

WORKDIR /app

# Copia os manifestos de pacotes e instala as dependências.
# O cache do Docker é aproveitado, reconstruindo esta camada apenas se os pacotes mudarem.
COPY package.json package-lock.json ./
RUN npm install

# Copia o restante do código-fonte.
COPY . .

# Aumenta o limite de memória para o processo Node.js para evitar erros de "heap out of memory".
ENV NODE_OPTIONS="--max-old-space-size=1024"

# Gera a build de produção. O nome 'frontend' deve corresponder ao nome do projeto em angular.json.
RUN npm run build -- --configuration production

# Stage 2: Production - Serve os arquivos estáticos com Nginx
FROM nginx:1.25-alpine

# Copia os arquivos da build do Angular para o diretório do Nginx.
COPY --from=build /app/dist/frontend/browser/ /usr/share/nginx/html

# Copia a configuração customizada do Nginx.
COPY nginx.conf /etc/nginx/conf.d/default.conf