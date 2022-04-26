from distutils.log import debug
from imp import reload
from pipes import Template
from tensorflow.keras.applications import imagenet_utils
from fastapi import FastAPI, File, Request, UploadFile
import tensorflow as tf
import numpy as np
import cv2
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uuid

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(
    directory="/home/rafiq/Rafiq/image_classification/mobilenet/templates")

# frame = cv2.imread("static/cute1.jpg")
# frame = cv2.resize(frame,(224, 224))
# frame = np.expand_dims(frame,axis=0)
# frame = tf.keras.applications.mobilenet.preprocess_input(frame)

# mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
# predictions = mobile.predict(frame)


# clissify = imagenet_utils.decode_predictions(predictions)

# print(clissify)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/file", response_class=HTMLResponse)
def read_root(request: Request, file: UploadFile = File(...)):
    # print(file.filename)
    file_name = f"./static/{uuid.uuid4().hex}.{file.filename.split('.')[1]}"
    with open(file_name, "wb") as f:
        f.write(file.file.read())
    frame = cv2.imread(file_name)
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0)
    frame = tf.keras.applications.mobilenet.preprocess_input(frame)
    mobile = tf.keras.applications.mobilenet_v2.MobileNetV2()
    predictions = mobile.predict(frame)
    clissify = imagenet_utils.decode_predictions(predictions)
    # print(type(clissify))
    # print(frame.shape)
    clissify_data={}
    for c in clissify[0]:
        clissify_data[c[1]]=c[2]
    print(clissify_data)
    return templates.TemplateResponse("index.html", {"request": request, "file_name": file_name, "clissify": clissify_data})


if __name__ == "__main__":
    uvicorn.run(app)

