
import sys
sys.path.append('/home/intisar/.local/lib/python3.6/site-packages')
sys.path.append("/home/intisar/Hasan/Deploy-edge-device")
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



def generate_key(id_len=16):
    ids = uuid.uuid4().hex[:id_len].lower()
    return ids
    
def image_to_base(frame):
    retval, buffer = cv2.imencode('.jpg', frame)
    base = base64.b64encode(buffer).decode('utf8')
    return base

def start(conf, args):
	if conf['detector']=="mtcnn":
		print("loaded MTCNN")
		detector = Detection()
	else:
		# ratina detector
		detector = Detection()
	in_cap = cv2.VideoCapture(conf["in_camera_id"])
	in_cap.set(3, conf["camera_resolution"][0])
	in_cap.set(4, conf["camera_resolution"][1])

	out_cap = cv2.VideoCapture(conf["out_camera_id"])
	out_cap.set(3, conf["camera_resolution"][0])
	out_cap.set(4, conf["camera_resolution"][1])

	save_data_id_edge_device = conf["save_data_in_edge_device"]

	if save_data_id_edge_device:
		os.makedirs(conf["save_path"]+"/in_single/",  exist_ok=True)
		os.makedirs(conf["save_path"]+"/out_single/", exist_ok=True)
    
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
						cv2.imwrite(conf["save_path"]+"/in_single/"+str(now)+".jpg", in_cropped_face)
					payload = json.dumps({
						"camera": "in",
						"photo": image_to_base(in_frame)
					})
					web_response_send = requests.request("POST", conf['web_server_address'], headers=conf["headers"], data=payload)
					if args.verbose:
						print("in_cam",web_response_send.text)

			# if detected face from exit camera
			if is_out:
				exit_frame = cv2.cvtColor(exit_cam, cv2.COLOR_BGR2RGB)
				out_cropped_face, bbox = detector.get_cropped_face(exit_frame)
				if out_cropped_face is not None:
					out_cropped_face = np.array(out_cropped_face)
					if save_data_id_edge_device:
						cv2.imwrite(conf["save_path"]+"/out_single/"+str(now)+".jpg", out_cropped_face)
					payload = json.dumps({
						"camera": "in",
						"photo": image_to_base(exit_frame)
					}) 
					web_response_send = requests.request("POST", conf['web_server_address'], headers=conf["headers"], data=payload)
					if args.verbose:
						print("out_cam",web_response_send.text)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		except Exception as e:
			print(e)
			continue

	in_cap.release()
	out_cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--show",  action="store_true",
                    help="show the faces in this device?")
	parser.add_argument("-v", "--verbose", action="store_true",
                    help="print the response")
	args = parser.parse_args()
	print(args)
	conf = get_edge_device_config()
	start(conf, args)
    
