#!/bin/bash
cd "$(dirname "$0")"

kubectl create namespace adminer
kubectl create -f deployment-new.yaml
