#Deploy Jenkins server for tests
import os
os.system('kubectl create -f pv-jenkins-home.yaml')
os.system('kubectl create -f pvc-jenkins-home.yaml')
os.system('kubectl create -f deployment.yaml')
os.system('kubectl create -f service.yaml')
