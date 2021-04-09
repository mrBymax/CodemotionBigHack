from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import cv2


model = ResNet50(weights='/script/neuralNet/resnet50_weights_tf_dim_ordering_tf_kernels.h5')


def predict_from_rgb(img):
    global model
    im_rgb = cv2.cvtColor(img, cv2.COLOR_RG2RGB)
    im_rgb = cv2.resize(im_rgb, (224, 224))
    x = im_rgb
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    return decode_predictions(preds, top=3)[0]


def predict(img):
    global model
    im_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    im_rgb = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2RGB)
    im_rgb = cv2.resize(im_rgb, (224, 224))
    x = im_rgb
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    return decode_predictions(preds, top=3)[0]
