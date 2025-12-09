#!/bin/bash

# Script de Inicialização Let's Encrypt
# Resolve o problema: Nginx precisa de certificados para iniciar,
# mas Certbot precisa do Nginx rodando para obter certificados

# Carrega variáveis de ambiente
if [ ! -f .env ]; then
    echo "Erro: Arquivo .env não encontrado!"
    exit 1
fi

source .env

# Configurações
DOMAINS=(${CERTBOT_DOMAIN} www.${CERTBOT_DOMAIN})
RSA_KEY_SIZE=4096
DATA_PATH="./certbot"
EMAIL=${CERTBOT_EMAIL}
STAGING=${CERTBOT_STAGING:-0}  # 0=production, 1=staging

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Inicializando Let's Encrypt para ${DOMAINS[0]} ===${NC}\n"

# Verifica se certificados já existem
if [ -d "$DATA_PATH/conf/live/${DOMAINS[0]}" ]; then
    echo -e "${YELLOW}Certificados existentes encontrados para ${DOMAINS[0]}${NC}"
    read -p "Deseja substituí-los? (y/N) " decision
    if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
        echo "Operação cancelada."
        exit 0
    fi
fi

# Baixa configurações recomendadas do Certbot se não existirem
if [ ! -e "$DATA_PATH/conf/options-ssl-nginx.conf" ] || [ ! -e "$DATA_PATH/conf/ssl-dhparams.pem" ]; then
    echo -e "${YELLOW}Baixando configurações SSL recomendadas...${NC}"
    mkdir -p "$DATA_PATH/conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$DATA_PATH/conf/options-ssl-nginx.conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$DATA_PATH/conf/ssl-dhparams.pem"
    echo
fi

# Cria certificados dummy para permitir que o Nginx inicie
echo -e "${YELLOW}Criando certificados dummy para ${DOMAINS[0]}...${NC}"
PATH_CERT="$DATA_PATH/conf/live/${DOMAINS[0]}"
mkdir -p "$PATH_CERT"
docker-compose --profile prod run --rm --entrypoint "\
    openssl req -x509 -nodes -newkey rsa:$RSA_KEY_SIZE -days 1 \
    -keyout '/etc/letsencrypt/live/${DOMAINS[0]}/privkey.pem' \
    -out '/etc/letsencrypt/live/${DOMAINS[0]}/fullchain.pem' \
    -subj '/CN=localhost'" certbot
echo

# Inicia o Nginx com certificados dummy
echo -e "${YELLOW}Iniciando Nginx...${NC}"
docker-compose --profile prod up --force-recreate -d nginx
echo

# Aguarda Nginx estar pronto
echo -e "${YELLOW}Aguardando Nginx iniciar...${NC}"
sleep 5

# Deleta certificados dummy
echo -e "${YELLOW}Deletando certificados dummy...${NC}"
docker-compose --profile prod run --rm --entrypoint "\
    rm -rf /etc/letsencrypt/live/${DOMAINS[0]} && \
    rm -rf /etc/letsencrypt/archive/${DOMAINS[0]} && \
    rm -rf /etc/letsencrypt/renewal/${DOMAINS[0]}.conf" certbot
echo

# Solicita certificado real do Let's Encrypt
echo -e "${GREEN}Solicitando certificado SSL do Let's Encrypt...${NC}"

# Monta o comando de domínios
DOMAIN_ARGS=""
for DOMAIN in "${DOMAINS[@]}"; do
    DOMAIN_ARGS="$DOMAIN_ARGS -d $DOMAIN"
done

# Escolhe servidor staging ou production
if [ $STAGING != "0" ]; then
    STAGING_ARG="--staging"
    echo -e "${YELLOW}ATENÇÃO: Usando servidor STAGING do Let's Encrypt${NC}"
else
    STAGING_ARG=""
    echo -e "${GREEN}Usando servidor PRODUCTION do Let's Encrypt${NC}"
fi

docker-compose --profile prod run --rm --entrypoint "\
    certbot certonly --webroot -w /var/www/certbot \
    $STAGING_ARG \
    $DOMAIN_ARGS \
    --email $EMAIL \
    --rsa-key-size $RSA_KEY_SIZE \
    --agree-tos \
    --no-eff-email \
    --force-renewal" certbot
echo

# Verifica se o certificado foi obtido com sucesso
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Certificado SSL obtido com sucesso!${NC}"

    # Recarrega o Nginx para usar o certificado real
    echo -e "${YELLOW}Recarregando Nginx...${NC}"
    docker-compose --profile prod exec nginx nginx -s reload

    echo -e "\n${GREEN}=== Configuração SSL concluída com sucesso! ===${NC}"
    echo -e "${GREEN}Seu site está disponível em https://${DOMAINS[0]}${NC}\n"
else
    echo -e "${RED}Erro ao obter certificado SSL!${NC}"
    echo -e "${YELLOW}Verifique os logs acima para detalhes.${NC}"
    exit 1
fi
