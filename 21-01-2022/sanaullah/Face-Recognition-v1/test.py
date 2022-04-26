from main.face_api_video import RECOG
import cv2

recog =RECOG()



cap=cv2.VideoCapture(0)
while True:
    _,f=cap.read()
    try:
        r = recog.recognition(f)
        print("rrrrrrrrrrrrr",r)
    except:
        continue
    cv2.imshow("V",r)
    cv2.waitKey(1) 

