#!/bin/sh

# Aborta o script se qualquer comando falhar
set -e

echo "Aguardando o banco de dados..."

# O netcat (nc) verifica se a porta 5432 do host 'db' está aberta.
# O loop continua até que o banco de dados aceite conexões.
while ! nc -z db 5432; do
  sleep 0.1
done

echo "Banco de dados iniciado"

python manage.py migrate

# Coleta os arquivos estáticos para a pasta /app/staticfiles
python manage.py collectstatic --noinput

# Executa o comando passado para o entrypoint (CMD do Dockerfile ou command do Compose)
exec "$@"