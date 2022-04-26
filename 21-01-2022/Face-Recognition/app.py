from logging import debug
from fastapi import FastAPI
from scipy.spatial.distance import jaccard
import uvicorn
import cv2
from ml.main.face_api_video import RECOG


recog =RECOG()



app = FastAPI()



@app.get("/")
def read_root():
    cap = cv2.VideoCapture(0)
    while True:
        try:
            _,frame = cap.read()
            recognition = recog.recognition(frame)
        except:
            continue
        print(recognition)
        cv2.imshow('frame', recognition)
        cv2.waitKey(1)
    return {"Hello": "World"}




















if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, debug=True , log_level="info")