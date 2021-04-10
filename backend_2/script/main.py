import random

from flask import Flask, request, send_from_directory, Response
from flask_cors import CORS, cross_origin

import cv2
import numpy as np
import json

from utils import image
from database import databaseHandler
# import matplotlib
# import matplotlib.pyplot as plt

# matplotlib.use('TkAgg')
import time
from neuralNet import predict as nnPredict
from database import databaseHandler

app = Flask(__name__, static_url_path='')
CORS(app)

devices = [
    {"class": "mouse",
     "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/29/c3/4a/0e/6d/b0/44/aa/peripherals_mouse_image/files/peripherals_mouse.jpg/_jcr_content/translations/en.peripherals_mouse.jpg"},
    {"class": "laptop",
     "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/72/cd/d6/b5/9a/a8/4e/63/computers_peripherals_laptop_image/files/computers_peripherals_laptop.jpg/_jcr_content/translations/en.computers_peripherals_laptop.jpg"},
    {"class": "notebook",
     "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/72/cd/d6/b5/9a/a8/4e/63/computers_peripherals_laptop_image/files/computers_peripherals_laptop.jpg/_jcr_content/translations/en.computers_peripherals_laptop.jpg"},
    {
        "class": "desktop_computer",
        "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group1/8b/3c/e1/eb/05/9d/4f/90/computers_peripherals_desktop_image/files/computers_peripherals_desktop.jpg/_jcr_content/translations/en.computers_peripherals_desktop.jpg"
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
            url = "none"
            for device in devices:
                if device["class"] == pred[1]:
                    url = device["imgEndpoint"]
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
    query = request.json['query']

    ret = []
    for device in devices:
        if device["class"] in query:
            ret.append(device)

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/classify/getInfo/<device>", methods=['GET'])
def getInfo(device):
    ret = databaseHandler.get_component(device)

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/teaching/getAllDevices", methods=['GET'])
def getAllDevices():
    # funzione Federico
    ret = databaseHandler.get_all_devices()
    # ret = [
    #     {
    #         "name": "test"
    #     },
    # ]

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


TEST_OPTIONS = {
    "device": "",
    "components": [],
    "block_diagram": []
}
CORRECT = {
    "components": [],
    "block_diagram": []
}
WRONG = {
    "components": [],
    "block_diagram": []
}


@app.route("/v1/teaching/setDevice/<device>", methods=['GET'])
def setComponent(device):
    global TEST_OPTIONS, CORRECT, WRONG
    CORRECT["components"] = databaseHandler.get_component(device)
    WRONG["components"] = databaseHandler.get_random_components(len(CORRECT["components"]), CORRECT["components"])

    TEST_OPTIONS["components"] = CORRECT + WRONG
    random.shuffle(TEST_OPTIONS["components"])
    TEST_OPTIONS["device"] = device

    # Todo: add block_diagram

    ret = {
        "detail": "Device set",
        "correct": CORRECT,
        "wrong": WRONG,
        "test": TEST_OPTIONS
    }
    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/teaching/getTest", methods=['GET'])
def getTest():
    resp = Response(response=json.dumps(TEST_OPTIONS),
                    status=200,
                    mimetype="application/json")
    return resp

@app.route("/v1/teaching/getBlockDiagram", methods=['GET'])
def getTest():
    resp = Response(response=json.dumps(TEST_OPTIONS),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
