docker run --rm -it \
-v "$PWD/script":/script \
-v "$PWD/frontend":/frontend \
-p 8083:5000 \
--name CMbackend \
-e FLASK_DEBUG=true \
--volume="/etc/group:/etc/group:ro" \
--volume="/etc/passwd:/etc/passwd:ro" \
--volume="/etc/shadow:/etc/shadow:ro" \
--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--user=$(id -u) \
--env="DISPLAY" \
cm_backend:dev python3 main.py
