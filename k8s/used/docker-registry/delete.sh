#!/bin/bash
kubectl delete namespace docker-registry
kubectl delete pv docker-registry-storage
kubectl delete pv docker-registry-certs
