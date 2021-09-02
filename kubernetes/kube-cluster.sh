#!/bin/bash

YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${YELLOW}Creating cluster using Kubeadm...${NC}"

kubeadm init --pod-network-cidr=192.168.0.0/16
export KUBECONFIG=/etc/kubernetes/admin.conf

echo ""
echo -e "${YELLOW}Applying pod network add-on Antrea...${NC}"
kubectl apply -f https://raw.githubusercontent.com/antrea-io/antrea/main/build/yamls/antrea.yml

watch kubectl get pods -A