#!/bin/bash

kind create cluster --config=kind-api-server.yaml
kind create cluster --config=kind-api-nginx.yaml