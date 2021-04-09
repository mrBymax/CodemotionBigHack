docker run --rm \
-v "$PWD/src":/usr/src/app/ \
-v "$PWD/data":/data \
-p 3032:3032 \
--name CM_backend \
CM_backend:dev