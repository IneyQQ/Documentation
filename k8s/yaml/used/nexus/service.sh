#!/bin/bash
kubectl expose deployment nexus --type=LoadBalancer --name=nexus-service --namespace=nexus

