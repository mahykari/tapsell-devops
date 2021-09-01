#!/bin/bash

YELLOW='\033[1;33m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${YELLOW}Removing Docker packages...${NC}"

apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli containerd.io
apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

echo ""
echo -e "${YELLOW}Removing Docker related files...${NC}"
rm -rf /var/lib/docker /etc/docker
rm /etc/apparmor.d/docker
groupdel docker
rm -rf /var/run/docker.sock
rm -rf /etc/apt/sources.list.d/docker.list