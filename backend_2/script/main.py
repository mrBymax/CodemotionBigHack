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

    ret = [
        {
            "found": True,
            "class": "Mouse",
            "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
            "score": 0.96
        },
        {
            "found": True,
            "class": "Mouse",
            "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
            "score": 0.95
        }
    ]
    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/v1/classify/classifyText')
def retFile(path):
    ret = [
        {
            "found": True,
            "class": "Mouse",
            "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
            "score": 0.96
        },
        {
            "found": True,
            "class": "Mouse",
            "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
            "score": 0.95
        }
    ]
    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/classify/getInfo/<path:path>")
def getInfo(path):
    print(path)
    ret =[
        {
            "componentName": "BALF-NRG-02D3",
            "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
        },
        {
            "componentName": "BALF-d-02D3",
            "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
        },
        {
            "componentName": "BALF-NRG-444",
            "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
        },
        {
            "componentName": "BALF-5523456-02D3",
            "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
        },
        {
            "componentName": "BALF-234567-02D3",
            "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
        }
    ]
    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
