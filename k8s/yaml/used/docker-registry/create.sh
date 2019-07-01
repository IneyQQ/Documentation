#!/bin/bash

cd "$(dirname "$0")"

kubectl create namespace docker-registry
kubectl create -f pv-certs.yaml
kubectl create -f pvc-certs.yaml
kubectl create -f pv-storage.yaml
kubectl create -f pvc-storage.yaml
kubectl create -f pv-auth.yaml
kubectl create -f pvc-auth.yaml
kubectl create -f deployment.yaml
