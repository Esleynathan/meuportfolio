# Stage 1: Build - Compila a aplicação Angular
FROM node:20-alpine AS build

WORKDIR /app

# Copia os manifestos de pacotes para aproveitar o cache do Docker.
COPY package.json package-lock.json ./

# Instala as dependências. O .dockerignore impede que a node_modules local seja copiada.
RUN npm install

# Copia o restante do código-fonte.
COPY . .

# Aumenta o limite de memória para o processo Node.js para evitar erros de "heap out of memory".
ENV NODE_OPTIONS="--max-old-space-size=1024"

# Gera a build de produção.
RUN npm run build -- --configuration production

# Stage 2: Production - Serve os arquivos estáticos com Nginx
FROM nginx:1.25-alpine

# Copia os arquivos da build do Angular para o diretório do Nginx.
# O caminho 'dist/frontend' corresponde ao 'outputPath' no angular.json.
COPY --from=build /app/dist/frontend/ /usr/share/nginx/html

# Copia a configuração customizada do Nginx.
COPY nginx.conf /etc/nginx/conf.d/default.conf