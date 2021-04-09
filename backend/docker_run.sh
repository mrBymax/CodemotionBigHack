docker run --rm \
-v "$PWD/src":/usr/src/app/ \
-v "$PWD/our_src/swagger_server/controllers":/usr/src/app/swagger_server/controllers \
-v "$PWD/our_src/swagger_server/libs":/usr/src/app/swagger_server/libs \
-v "$PWD/data":/data \
-p 8083:8080 \
--name CMbackend \
--env DISPLAY=unix$DISPLAY  \
--privileged --volume $XAUTH:/root/.Xauthority \
--volume /tmp/.X11-unix:/tmp/.X11-unix \
-e FLASK_DEBUG=true \
cm_backend:dev
