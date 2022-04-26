from matplotlib import image
from mlutils.src.main import ALL_FUNCTIONS
import cv2
import base64
import numpy as np
import random
from django.conf import settings

from project.settings import MEDIA_ROOT


recog = ALL_FUNCTIONS()


def convert_to_im_array(data):
    arr = base64.b64decode(data)
    img_arr = np.frombuffer(arr, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    return img


def image_to_base(frame):
    retval, buffer = cv2.imencode('.jpg', frame)
    base = base64.b64encode(buffer).decode('utf8')
    return base


def registration_new_face(file, name_id):
    frame = convert_to_im_array(file)
    name = name_id.replace(" ", "-")
    response = recog.registration(frame, name)
    if response == 200:
        return {"status": 200}
    if response == 500:
        return {"status": 400}
    else:
        return {"status": 500}


def recognition_face(file):
    response = recog.recognition(convert_to_im_array(file))
    name = response['result'][0]
    frame = response['result'][1]
    if name == "multiple faces detected":
        return {"message":"you have more than one face","status":201}
    if frame is not None:
        imag_name = str(name+str(random.randint(0000,9999)))
        imagePath = f"{MEDIA_ROOT}/{imag_name}.png"
        cv2.imwrite(imagePath,frame)
        return {"name":name,"image":imag_name,"status":200}
    else:
        return {"message":"Matched face not found Please register first","status":501}