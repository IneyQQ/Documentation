source env.sh

openssl req \
  -newkey rsa:4096 -nodes -sha256 -keyout $location/certs/domain.key \
  -x509 -days 3650 -out $location/certs/domain.crt
# Returns CA certificate for clients. Save it to ca.crt and add to client side
openssl s_client -showcerts -verify 5 -connect docker-lsbt.iba:32000 < /dev/null