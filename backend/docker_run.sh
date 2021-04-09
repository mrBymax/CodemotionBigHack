docker run --rm \
-v "$PWD/src":/usr/src/app/ \
-v "$PWD/our_src/swagger_server/controllers":/usr/src/app/swagger_server/controllers \
-v "$PWD/data":/data \
-p 8083:8080 \
--name CMbackend \
cm_backend:dev