#!/bin/bash

cd "$(dirname "$0")"

kubectl create namespace nexus
kubectl create -f pv-nexus.yaml
kubectl create -f pvc-nexus.yaml
kubectl create -f deployment.yaml
