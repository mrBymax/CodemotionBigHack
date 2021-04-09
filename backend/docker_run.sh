docker run --rm \
-v "$PWD/src":/usr/src/app/ \
-v "$PWD/data":/data \
-p 8083:8080 \
--name CMbackend \
cm_backend:dev