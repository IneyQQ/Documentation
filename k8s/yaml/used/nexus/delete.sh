#!/bin/bash

cd "$(dirname "$0")"

kubectl delete namespace nexus
kubectl delete -f pv-nexus.yaml
