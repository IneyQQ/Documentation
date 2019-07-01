#!/bin/bash

cd "$(dirname "$0")"

kubectl create namespace nagios
kubectl create -f pv.yaml
kubectl create -f pvc.yaml
kubectl create -f deployment.yaml
