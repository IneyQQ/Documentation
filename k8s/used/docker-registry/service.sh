#!/bin/bash
kubectl expose deployment docker-registry --type=LoadBalancer --name=docker-registry-service --namespace=docker-registry
