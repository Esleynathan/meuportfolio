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

# Usa configuração HTTP-only temporária para obtenção inicial de certificados
echo -e "${YELLOW}Configurando Nginx em modo HTTP-only para obtenção de certificados...${NC}"
if [ ! -f "frontend/nginx.conf.backup" ]; then
    cp frontend/nginx.conf frontend/nginx.conf.backup
    echo -e "${GREEN}Backup da configuração SSL criado em nginx.conf.backup${NC}"
fi
cp frontend/nginx.init.conf frontend/nginx.conf
echo

# Para containers existentes
echo -e "${YELLOW}Parando containers existentes...${NC}"
docker compose --profile prod down
echo

# Reconstrói e inicia o Nginx com configuração HTTP-only
echo -e "${YELLOW}Reconstruindo Nginx com configuração HTTP-only...${NC}"
docker compose --profile prod build --no-cache nginx
echo

echo -e "${YELLOW}Iniciando Nginx em modo HTTP-only...${NC}"
docker compose --profile prod up -d nginx
echo

# Aguarda Nginx estar pronto
echo -e "${YELLOW}Aguardando Nginx iniciar...${NC}"
sleep 5

# Verifica se Nginx está rodando
if ! docker compose --profile prod ps nginx | grep -q "Up"; then
    echo -e "${RED}Erro: Nginx não iniciou corretamente!${NC}"
    docker compose --profile prod logs nginx
    exit 1
fi
echo -e "${GREEN}Nginx rodando em modo HTTP-only${NC}"
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
    echo

    # Restaura configuração SSL completa
    echo -e "${YELLOW}Restaurando configuração Nginx com suporte SSL...${NC}"
    cp frontend/nginx.conf.backup frontend/nginx.conf
    echo

    # Reconstrói Nginx com configuração SSL
    echo -e "${YELLOW}Reconstruindo Nginx com configuração SSL...${NC}"
    docker compose --profile prod build --no-cache nginx
    echo

    # Reinicia Nginx com a configuração SSL
    echo -e "${YELLOW}Reiniciando Nginx com SSL habilitado...${NC}"
    docker compose --profile prod up -d --force-recreate nginx
    echo

    # Aguarda Nginx reiniciar
    sleep 5

    # Verifica se Nginx está rodando com SSL
    if docker compose --profile prod ps nginx | grep -q "Up"; then
        echo -e "${GREEN}Nginx rodando com SSL habilitado!${NC}"
        echo -e "\n${GREEN}=== Configuração SSL concluída com sucesso! ===${NC}"
        echo -e "${GREEN}Seu site está disponível em:${NC}"
        echo -e "${GREEN}  - https://${DOMAINS[0]}${NC}"
        echo -e "${GREEN}  - https://www.${DOMAINS[0]} (redireciona para versão sem www)${NC}\n"
    else
        echo -e "${RED}Erro: Nginx não iniciou com SSL!${NC}"
        docker compose --profile prod logs nginx
        exit 1
    fi
else
    echo -e "${RED}Erro ao obter certificado SSL!${NC}"
    echo -e "${YELLOW}Verifique os logs acima para detalhes.${NC}"
    echo -e "${YELLOW}Restaurando configuração original...${NC}"
    if [ -f "frontend/nginx.conf.backup" ]; then
        cp frontend/nginx.conf.backup frontend/nginx.conf
    fi
    exit 1
fi
