from fastapi import APIRouter
from starlette.requests import Request
import cv2
import base64
import numpy as np
from datetime import datetime
from project.src.main import ALL_FUNCTIONS
now = datetime.now()

detcotor =ALL_FUNCTIONS()

router = APIRouter()



def convert_to_im_array(data):
    arr = base64.b64decode(data)
    img_arr = np.frombuffer(arr, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    return img






# @router.get("/")
# def home():
#     image = cv2.imread("/home/sanaullah/microservice/project/mun.jpeg")
#     data = detcotor.registration(image, "0050")
#     print("gggg",data)
#     return {"message":"hello World"}

# # For detection
# @router.post("/frame")
# async def index(request:Request):
#     data = await  request.json()
#     frame = data["frame"]
#     image = convert_to_im_array(frame)
#     # cv2.imwrite("./"+str(now)+".png", image)
#     face,_,_ = detcotor.detection(image)
#    # cv2.imwrite("./"+str(now)+"_face"+".jpg", face[0])

#     return {"message":"200"}





@router.post("/recognition")
async def recognition(request:Request):
    data = await request.json()
    frame = data["frame"]
    image = convert_to_im_array(frame)

    data = detcotor.recognition(image)
    return data

