#!/bin/bash

YELLOW='\033[1;33m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${YELLOW}Applying api-server config file in Kubernetes...${NC}"

kubectl config set-context kind-api-server

kubectl apply -f kube-api-server.yaml
ret1=$?

echo ""
echo -e "${YELLOW}Applying api-nginx config file in Kubernetes...${NC}"

kubectl apply -f kube-api-nginx.yaml
ret2=$?

if [ $ret1 -eq 0 ] && [ $ret2 -eq 0 ]; then
    echo -e "${GREEN}Configs successfully applied${NC}"
else
    echo -e "${RED}Configs failed${NC}"
fi