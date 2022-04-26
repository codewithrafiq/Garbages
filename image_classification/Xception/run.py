from fastapi import FastAPI, File, Request, UploadFile
import tensorflow as tf
import numpy as np
import cv2
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uuid
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing import image

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(
    directory="/home/rafiq/Rafiq/image_classification/Xception/templates")



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/file", response_class=HTMLResponse)
def read_root(request: Request, file: UploadFile = File(...)):
    print(file.filename)
    file_name = f"./static/{uuid.uuid4().hex}.{file.filename.split('.')[1]}"
    with open(file_name, "wb") as f:
        f.write(file.file.read())
        
    clissify_data={}
    for c in clissify[0]:
        clissify_data[c[1]]=c[2]

    return templates.TemplateResponse("index.html", {"request": request, "file_name": file_name, "clissify": clissify_data})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
