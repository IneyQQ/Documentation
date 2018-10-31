#!/bin/bash

cd "$(dirname "$0")"

kubectl create namespace mysql
kubectl create -f pv-data.yaml
kubectl create -f pvc-data.yaml
kubectl create -f pv-conf.yaml
kubectl create -f pvc-conf.yaml
kubectl create secret generic mysql-root --from-literal=password_root=Passw0rd --namespace=mysql
#kubectl create secret generic mysql-dev --from-literal=password_liferay_dev=life21ray! --namespace=mysql
kubectl create -f deployment.yaml
kubectl expose deployment mysql-dev --type=LoadBalancer --name=mysql-dev --namespace=mysql
