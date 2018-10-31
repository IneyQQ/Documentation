#!/bin/bash
kubectl expose deployment mysql-dev --type=LoadBalancer --name=mysql-dev-service --namespace=mysql
