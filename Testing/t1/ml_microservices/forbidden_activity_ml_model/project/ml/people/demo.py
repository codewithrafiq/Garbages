import cv2
import scipy.io as sio
import os
from project.ml.people.centerface import CenterFace
import math
import time

class PEOPLE:
    def __init__(self):
        self.centerface = CenterFace()

    def count_number(self, frame):
        
        h, w = frame.shape[:2]
        if frame is not None:
            dets, lms = self.centerface(frame, h, w, threshold=0.35)
            return (len(dets))
            
            
                
            