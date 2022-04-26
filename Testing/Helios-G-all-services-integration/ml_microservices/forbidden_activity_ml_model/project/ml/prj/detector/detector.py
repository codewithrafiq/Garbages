import cv2
import scipy.io as sio
import os
from project.ml.prj.detector.centerface import CenterFace
import math
# from prj.detector.align_trans import get_reference_facial_points, warp_and_crop_face
import numpy as np
import time
import datetime
# reference = get_reference_facial_points(default_square= True)


class ABSENSE:

    def __init__(self):
        self.centerface = CenterFace()
        
    def count_number(self, frame):
  
        h, w = frame.shape[:2]
        centerface = CenterFace()
        dets, lms = centerface(frame, h, w, threshold=0.5)
        for det in dets:
            boxes, score = det[:4], det[4]
            # print(boxes[0])
            cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)
            img =frame[int(boxes[1]):int(boxes[1])+int(boxes[3]),int(boxes[0]):int(boxes[0])+int(boxes[2])]
            # cv2.imwrite("frame.png",img)
        

        return len(dets)


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
                dist = self.distance(xx[0],xx[2],xx[1],xx[3])
                if dist is not None:

                    return dist
             
                else:
                    return dist
