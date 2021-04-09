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
from neuralNet import predict as nnPredict

app = Flask(__name__, static_url_path='')
CORS(app)


devices = [
    {"name": "mouse",
     "url": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/29/c3/4a/0e/6d/b0/44/aa/peripherals_mouse_image/files/peripherals_mouse.jpg/_jcr_content/translations/en.peripherals_mouse.jpg"},
    {"name": "laptop",
     "url": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/72/cd/d6/b5/9a/a8/4e/63/computers_peripherals_laptop_image/files/computers_peripherals_laptop.jpg/_jcr_content/translations/en.computers_peripherals_laptop.jpg"},
    {"name": "notebook",
    "url": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/72/cd/d6/b5/9a/a8/4e/63/computers_peripherals_laptop_image/files/computers_peripherals_laptop.jpg/_jcr_content/translations/en.computers_peripherals_laptop.jpg"},
    {
        "name": "desktop_computer",
        "url": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/8b/3c/e1/eb/05/9d/4f/90/computers_peripherals_desktop_image/files/computers_peripherals_desktop.jpg/_jcr_content/translations/en.computers_peripherals_desktop.jpg"
    }
]


@app.route('/v1/classify/classifyImage', methods=['POST'])
def predict():
    img = request.json['image_b64']
    img = str(img)

    img = img.split(',')[1]  # Extract base64
    img = image.getImg(img)  # Converts into RGB

    res = nnPredict.predict(img)
    ret = []

    if len(res) > 0:
        for pred in res:
            for device in devices:
                if device["name"] == pred[1]:
                    url = device["url"]
                    break

            ret.append({
                "class": pred[1],
                "imgEndpoint": url,
                "score": float(pred[2])
            })
    print(ret)
    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/v1/classify/classifyText', methods=['POST'])
def retFile():
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


@app.route("/v1/classify/getInfo/<path:path>", methods=['GET'])
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
