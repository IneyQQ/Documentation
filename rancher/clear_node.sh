docker rm -f $(docker ps -qa)
docker volume rm etcd
rm -r /var/etcd/backups/*
reboot
rm -rf /var/lib/rancher/state