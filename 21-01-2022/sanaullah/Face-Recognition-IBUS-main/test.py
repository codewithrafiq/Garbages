from face_api import RECOG
import cv2
import numpy as np

recog =RECOG()

image = cv2.imread("fr.jpeg")

recognition = recog.recognition(image)
print(recognition)