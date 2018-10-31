source env.sh

docker run\
	--name registry \
	-d \
	-p 5000:5000\
	-e REGISTRY_HTTP_ADDR=0.0.0.0:5000\
	-e REGISTRY_HTTP_TLS_CERTIFICATE=/docker/certs/domain.crt \
	-e REGISTRY_HTTP_TLS_KEY=/docker/certs/domain.key \
	-e REGISTRY_STORAGE_DELETE_ENABLED="true" \
	-e REGISTRY_AUTH=htpasswd \
	-e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" \
	-e REGISTRY_AUTH_HTPASSWD_PATH=/docker/auth/htpasswd \
	-v $location/certs:/docker/certs \
	-v $location/storage:/docker/storage \
	-v $location/auth:/docker/auth \
	registry