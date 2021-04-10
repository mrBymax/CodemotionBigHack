import random

import os
from flask import Flask, request, send_from_directory, Response
from flask_cors import CORS

import json

from utils import image
from database import databaseHandler

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
    },
    {
        "class": "ABS",
        "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/block_diagram/abs/files/abs.svg"
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
        if device["class"].lower() in query.lower():
            ret.append(device)

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/classify/getInfo/<device>", methods=['GET'])
def getInfo(device):
    global devices
    block_diagram_url = ""
    for _device in devices:
        if _device["class"].lower() in device.lower():
            block_diagram_url = _device["imgEndpoint"]
            break

    ret = [{
        "name": "Block diagram",
        "description": '<img src="'+block_diagram_url+'" width="500px" />'
    }]
    ret += databaseHandler.get_component(device)

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/teaching/getAllDevices", methods=['GET'])
def getAllDevices():
    ret = databaseHandler.get_all_devices()

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


@app.route("/v1/teaching/setDevice/<deviceName>", methods=['GET'])
def setComponent(deviceName):
    global TEST_OPTIONS, CORRECT, WRONG
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

    CORRECT["components"] = databaseHandler.get_component(deviceName)
    WRONG["components"] = databaseHandler.get_random_components(len(CORRECT["components"]), CORRECT["components"])

    TEST_OPTIONS["components"] = CORRECT["components"] + WRONG["components"]
    random.shuffle(TEST_OPTIONS["components"])
    TEST_OPTIONS["device"] = deviceName

    correct_url = ""
    # Todo: add block_diagram
    for device in devices:
        if device["class"].lower() in deviceName.lower():
            correct_url = device["imgEndpoint"]
            break

    CORRECT["block_diagram"].append(correct_url)

    devices2 = devices
    random.shuffle(devices2)
    i = 0
    for item in devices2:
        if i == 3:
            break
        if item["imgEndpoint"] != correct_url:
            WRONG["block_diagram"].append(item["imgEndpoint"])
            i += 1

    print(CORRECT["block_diagram"])
    print(WRONG["block_diagram"])

    TEST_OPTIONS["block_diagram"] = CORRECT["block_diagram"] + WRONG["block_diagram"]
    random.shuffle(TEST_OPTIONS["block_diagram"])

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


TESTS = []


@app.route("/v1/teaching/getSubmittedTests", methods=['GET'])
def getSubmittedTests():
    resp = Response(response=json.dumps(TESTS),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/v1/teaching/submitTest", methods=['POST'])
def submitTest():
    global TESTS
    test_data = request.json

    correct = 0
    wrong = 0

    for answer in test_data["data"]["answers"]:
        answer["expected"] = False
        for correct_component in CORRECT["components"]:
            if answer["component"] == correct_component["name"]:
                answer["expected"] = True
                break
        if answer["expected"] == answer["checked"]:
            correct += 1
        else:
            wrong += 1

    test_data["data"]["block_diagram"]["correct"] = False
    if test_data["data"]["block_diagram"]["url"] in CORRECT["block_diagram"]:
        test_data["data"]["block_diagram"]["correct"] = True

    test_data["data"]["block_diagram"]["correct_url"] = CORRECT["block_diagram"]

    test_data["score"] = {
        "correct": correct,
        "wrong": wrong
    }

    TESTS.append(test_data)

    ret = {
        "detail": "okay",
        "data": test_data
    }

    resp = Response(response=json.dumps(ret),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/', defaults=dict(filename=None))
@app.route('/<filename>', methods=['GET'])
def index(filename):
    print(filename)
    filename = filename or 'index.html'
    return send_from_directory('/frontend/', filename)


@app.route('/<path:dir1>/<path:filename>', methods=['GET'])
def index2(dir1, filename):
    filename = filename or 'index.html'
    return send_from_directory(os.path.join('/frontend', dir1), filename)


@app.route('/<path:dir1>/<path:dir2>/<path:filename>', methods=['GET'])
def index3(dir1, dir2, filename):
    filename = filename or 'index.html'
    return send_from_directory(os.path.join('/frontend', dir1, dir2), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
