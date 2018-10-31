#!/bin/bash
kubectl expose deployment nagios-test --type=LoadBalancer --name=nagios-test-service --namespace=nagios
