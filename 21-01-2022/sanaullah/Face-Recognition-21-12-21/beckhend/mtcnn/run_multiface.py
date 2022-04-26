import os
import cv2
import time
import uuid
import json
import base64
import requests
import numpy as np
from PIL import Image
from retina import Detection
from datetime import datetime
from config.conf import get_edge_device_config




def generate_key(id_len=16):
    ids = uuid.uuid4().hex[:id_len].lower()
    return ids
    
def image_to_base(frame):
    retval, buffer = cv2.imencode('.jpg', frame)
    base = base64.b64encode(buffer).decode('utf8')
    return base

def start(conf):
	
	detector = Detection()
	in_cap = cv2.VideoCapture(conf["in_camera_id"])
	in_cap.set(3, conf["camera_resolution"][0])
	in_cap.set(4, conf["camera_resolution"][1])

	out_cap = cv2.VideoCapture(conf["out_camera_id"])
	out_cap.set(3, conf["camera_resolution"][0])
	out_cap.set(4, conf["camera_resolution"][1])

	save_data_id_edge_device = conf["save_data_id_edge_device"]


	url = "http://20.212.16.129/api/perform-attendances/"
	#our_server = "http://103.239.252.215:80/officencnn"
	our_server = "http://52.163.71.151:80/officemulti"
	# if save_data_id_edge_device:
	# 	os.makedirs("in_single/",  exist_ok=True)
	# 	os.makedirs("out_single/", exist_ok=True)

    
	while True:
		now = datetime.now()

		is_in, in_cam    = in_cap.read()
		is_out, exit_cam = out_cap.read()

		try:
		    ## detection API
		    ## if detected face from front camera
			if is_in:
				in_frame = cv2.cvtColor(in_cam, cv2.COLOR_BGR2RGB)
				in_cropped_face, bbox = detector.get_cropped_face(in_frame)
				if in_cropped_face is not None:
					in_cropped_face = np.array(in_cropped_face)
					if save_data_id_edge_device:
						cv2.imwrite("in_single/"+str(now)+".jpg", in_cropped_face)

					payload_server = json.dumps({
						"token": "6daf758ba58545159330fb320482cc8z",
						"file": image_to_base(in_cam)
						})
					headers_server = {
							'Concent-Type': 'application/json'
						}

					server_response = requests.request("POST", our_server, headers=headers_server, data=payload_server)
					print(server_response.json())
					server_response = server_response.json()
					#cv2.imshow('InCam', in_cam)

			if is_out:
				exit_frame = cv2.cvtColor(exit_cam, cv2.COLOR_BGR2RGB)
				_, out_cropped_face =detector.get_cropped_face(exit_frame)
				if out_cropped_face is not None:
					out_cropped_face = np.array(out_cropped_face[0])
					if save_data_id_edge_device:
						cv2.imwrite("out_single/"+str(now)+".jpg", out_cropped_face)

					payload_server = json.dumps({
					"token": "6daf758ba58545159330fb320482cc8z",
					"file": image_to_base(exit_cam)
					})
					headers_server = {
						'Concent-Type': 'application/json'
					}

					server_response = requests.request("POST", our_server, headers=headers_server, data=payload_server)
					print(server_response.json())

					server_response_out = server_response.json() 
					print(server_response_out,"out")  
					#cv2.imshow('ExCam', exit_frame)     
		        
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		except Exception as e:
			print(e)
			continue
	in_cap.release()
	out_cap.release()
	cv2.destroyAllWindows()
conf = get_edge_device_config()
start(conf)
    
