
import sys
import os
import cv2
import time
import uuid
import json
import base64
import argparse
import requests
import numpy as np
from PIL import Image
from retina import Detection
from MTCNN import DetectionMtcnn
from datetime import datetime
from config.conf import get_edge_device_config

    
def image_to_base(frame):
    retval, buffer = cv2.imencode('.jpg', frame)
    base = base64.b64encode(buffer).decode('utf8')
    return base
path = "./mppp.mp4"

detector = DetectionMtcnn()
in_cap = cv2.VideoCapture(path)
in_cap.set(3,720 )
in_cap.set(4,720 )

while True:
	now = datetime.now()
	is_in, in_cam    = in_cap.read()
	try:
		if is_in: 
			in_frame = cv2.cvtColor(in_cam, cv2.COLOR_BGR2RGB)
			print(in_frame)
			in_cropped_face, bbox,_ = detector.get_cropped_face(in_frame)
			print(len(bbox))
			for face in in_cropped_face:
				cv2.imwrite("./known/"+str(now)+".png", face)
			for boxes in bbox:
				cv2.rectangle(in_cam,(boxes[0],boxes[1]), (boxes[0]+boxes[2], boxes[1]+boxes[3]),(255, 0, 0),2)
			print(bbox)
			cv2.imshow("face detector", in_cam)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	except Exception as e:
		print(e)
		continue

in_cap.release()
cv2.destroyAllWindows()

