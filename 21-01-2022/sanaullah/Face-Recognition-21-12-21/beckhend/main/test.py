from face_api import RECOG
import cv2
import numpy as np

recog =RECOG()

image = cv2.imread("./fr.jpeg")
print(image.shape)
recogn = recog.recognition(image)
print(recogn)