FROM dkimg/opencv:4.4.0-ubuntu

# FOR DISPLAY
RUN apt-get update
RUN apt-get install -qqy x11-apps libgtk2.0-dev

WORKDIR /script

RUN pip3 install connexion
RUN pip3 install Pillow
RUN pip3 install flask_cors
RUN pip3 install matplotlib
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y python3-tk
RUN pip3 install tk
COPY ./script/requirements.txt /script

RUN pip3 install --no-cache-dir -r requirements.txt

#ENTRYPOINT ["python3"]

#CMD ["-m", "swagger_server"]