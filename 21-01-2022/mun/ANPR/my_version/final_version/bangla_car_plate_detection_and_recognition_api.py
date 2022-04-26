

import os
import cv2
import json
import numpy 
import requests
import matplotlib
from PIL import Image
from datetime import datetime
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import bangla_v2_car_plate_detection_and_recognition as cnpdr
import matplotlib.pyplot as plt




app = Flask(__name__)   

#image extention check

app.config["IMAGE_UPLOADS"] = "Uploaded"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF",'png', 'jpg', 'jpeg']

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False  


 

# POST - GET the image and metadata
@app.route('/PlateRecognition', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		# print("got request")
		try:
			#client request store
			imagesave = request.files.get('image')
			# # auth= request.values.get('auth')
			if allowed_image(imagesave.filename):

				#convert image from string to array
				imagefile = imagesave.read()
				npimg = numpy.fromstring(imagefile, numpy.uint8)
				
				img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
				# vehicle_image = plt.imread(imagefile)
				# num_plate = cnpdr.plate_recognition(vehicle_image)
				num_plate = cnpdr.plate_recognition(img)
				resp_data={"Number Plate":num_plate}
				resp_data=json.dumps(resp_data)

			return resp_data



		except Exception : 

			resp_error = "Opps !! internal error try again!!"
			return resp_error

        
if __name__ == '__main__':
	app.run(debug = True,host='0.0.0.0',port=5000)
