# Use uma imagem Python slim para um tamanho final menor
FROM python:3.11-slim

# Define variáveis de ambiente para otimização e para que os logs apareçam imediatamente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema, como netcat e dos2unix.
# Unificar em uma única camada RUN melhora o cache e reduz o tamanho da imagem.
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd dos2unix && \
    rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências de produção
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Converte o entrypoint.sh para o formato Unix e o torna executável
RUN dos2unix /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Expõe a porta em que o Gunicorn será executado
EXPOSE 8000

# O comando para iniciar a aplicação é definido no docker-compose.yml para maior flexibilidade.
# No entanto, um CMD padrão é uma boa prática.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]