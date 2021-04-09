from flask import Flask, request, send_from_directory, Response
from flask_cors import CORS, cross_origin

import cv2
import numpy as np
import json

from utils import image
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import time

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/v1/classify/classifyImage', methods=['GET', 'POST'])
def predict():
    img = request.json['image_b64']
    img = str(img)

    img = img.split(',')[1]  # Extract base64
    img = image.getImg(img)  # Converts into RGB

    plt.imshow(img)
    plt.show()
    time.sleep(10)
    print("AS")

    ret = "ciao"
    resp = Response(response=ret,
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/<path:path>')
def retFile(path):
    return send_from_directory('static', path)


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
