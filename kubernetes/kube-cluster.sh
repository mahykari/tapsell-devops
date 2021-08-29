#!/bin/bash

YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo '$(YELLOW)Creating clusters using Kind...$(NC)'

kind create cluster --config=kind-api-server.yaml