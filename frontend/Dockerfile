# Stage 1: Build - Compila a aplicação Angular
# Usamos uma imagem Node com Alpine para um build mais leve.
FROM node:20-alpine AS build

# Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# Copia os arquivos de manifesto de pacotes primeiro para aproveitar o cache do Docker.
# Esta camada só será reconstruída se os pacotes mudarem.
COPY package.json package-lock.json ./

# Instala as dependências do projeto.
RUN npm install

# Copia o restante do código-fonte da aplicação.
COPY . .

# Gera a build de produção otimizada. O output será salvo em /app/dist/frontend/browser.
# O nome 'frontend' deve corresponder ao nome do seu projeto em angular.json.
RUN npm run build -- --configuration production

# Stage 2: Production - Serve os arquivos estáticos com Nginx
# Usamos uma imagem Nginx com Alpine, que é extremamente leve.
FROM nginx:1.25-alpine

# Copia os arquivos estáticos da build do Stage 1 para o diretório padrão do Nginx.
# O output do build do Angular 15+ fica em 'dist/project-name/browser'
COPY --from=build /app/dist/frontend/ /usr/share/nginx/html

# Copia a nossa configuração customizada do Nginx para o diretório de configurações do contêiner.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80 para o tráfego HTTP.
EXPOSE 80

# O comando para iniciar o Nginx e a configuração (nginx.conf) serão gerenciados
# pelo nosso docker-compose.yml e pelo Dockerfile final que o usará.
# Este Dockerfile é um passo intermediário, o final será ajustado.
# Por enquanto, o comando padrão do Nginx é suficiente.