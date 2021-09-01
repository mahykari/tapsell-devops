#!/bin/bash

YELLOW='\033[1;33m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

kubeadm reset

echo ""
echo -e "${YELLOW}Removing Kubernetes packages...${NC}"

apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*
apt-get autoremove

echo ""
echo -e "${YELLOW}Removing Kubernetes cofig directory...${NC}"
rm -rf ~/.kube