# Use uma imagem Python slim para um tamanho final menor
FROM python:3.11-slim

# Define variáveis de ambiente para otimização e para que os logs apareçam imediatamente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema, como o netcat para o entrypoint.sh
RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker.
# A camada só será reconstruída se o requirements.txt mudar.
COPY requirements.txt .

# Instala as dependências de produção
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY . .

# Copia o script de entrypoint e dá permissão de execução
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expõe a porta em que o Gunicorn será executado
EXPOSE 8000

# O comando para iniciar a aplicação é definido no docker-compose.yml para maior flexibilidade.
# No entanto, um CMD padrão é uma boa prática.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]