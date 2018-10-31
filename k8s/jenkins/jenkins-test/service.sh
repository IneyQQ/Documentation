#!/bin/bash
kubectl expose deployment jenkins-test --type=LoadBalancer --name=jenkins-test --namespace=jenkins
