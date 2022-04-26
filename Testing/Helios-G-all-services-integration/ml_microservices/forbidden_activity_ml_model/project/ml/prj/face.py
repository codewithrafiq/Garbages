import cv2
import scipy.io as sio
import os
from project.ml.prj.centerface import CenterFace
import math
from project.ml.prj.align_trans import get_reference_facial_points, warp_and_crop_face
import numpy as np


class Detector:
    def __init__(self):
        self.reference = get_reference_facial_points(default_square= True)
        self.centerface = CenterFace()


    def distance(self,x1,x2,y1, y2):
        
        dist = math.sqrt((x1-x2)**2-(y1-y2)**2)
        return dist


    def detection(self,frame):

        h, w = frame.shape[:2]
        dets, lms = self.centerface(frame, h, w, threshold=0.35)
        for det in dets:
            boxes, score = det[:4], det[4]
           # cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)
        for lm in lms:
            for i in range(0, 5):
                xx = lm
                r_landmarks = [[xx[2],xx[3]],[xx[0],xx[1]],[xx[4],xx[5]],[xx[8],xx[9]],[xx[6],xx[7]]]
                warped_face = warp_and_crop_face(np.array(frame), r_landmarks,self.reference, crop_size=(112,112))
                # print("############################",warped_face)
                dist = self.distance(xx[0],xx[2],xx[1],xx[3])
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@",dist)
                if dist is not None:

                    return dist, warped_face
             
                else:
                    return dist, None

