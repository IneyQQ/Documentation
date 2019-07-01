#!/bin/bash
kubectl expose deployment nagios-prod --type=LoadBalancer --name=nagios-service --namespace=nagios
