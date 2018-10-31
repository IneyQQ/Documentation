source env.sh

openssl req \
  -newkey rsa:4096 -nodes -sha256 -keyout $location/certs/domain.key \
  -x509 -days 3650 -out $location/certs/domain.crt