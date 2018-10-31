#!/bin/bash
kubectl expose deployment adminer --type=LoadBalancer --name=adminer --namespace=adminer
