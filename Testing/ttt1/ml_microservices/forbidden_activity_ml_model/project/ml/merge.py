import datetime
import time
from traceback import print_tb
from tracemalloc import start
from urllib import response
import cv2
import numpy as np
import base64

import pytz
from project.ml.absence import WORKER_COUNTER
from project.ml.face_recog.project.src.main import ALL_FUNCTIONS
from project.ml.yolo.yolo_video2 import FORBIDDEN_ACTIVITY
from project.ml.prj.face import Detector
import requests


class MERGE:

    def __init__(self):
        self.recog = ALL_FUNCTIONS()
        self.faa = FORBIDDEN_ACTIVITY()
        self.detect = Detector()
        self.cum_time = {}
        self.counter = WORKER_COUNTER()

    def convert_to_im_array(self, data):
        arr = base64.b64decode(data)
        img_arr = np.frombuffer(arr, np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        return img

    def image_to_base64(self, image):
        ret, jpeg = cv2.imencode('.jpg', image)
        return base64.b64encode(jpeg).decode('utf-8')

    def face_recognition(self, image):

        # data = self.convert_to_im_array(image)
        result = self.recog.recognition(image)
        return result

    def forbidden_activity(self, image):
        
        # print("Merge-forbidden_activity------------------->",image.shape)
        # activity, time, img, start_time, end_time = self.faa.activity(image)
        activity, time, img, start_time, end_time = self.faa.activity(image)
        # print("activity, time, img, start_time, end_time----->",activity, time, img, start_time, end_time)
        # print(activity, time)
        # cv2.imwrite("face.png",img)
        # if img is not None:
        #     print("image is not none")

        result = None
        if img.shape != None:
            print(img.shape)
            # result = self.recog.recognition(img)
            img_base64 = self.image_to_base64(img)
            # print("img_base64",img_base64)
            response = requests.post(
                "http://0.0.0.0:8889/recognition_frame/", json={"image": img_base64})
            # print("img_base64----->", result.json())
            response_data = response.json()
            result = response_data["name"]


        # print("forbidden_activity----", result)

        if result not in self.cum_time.keys():
            self.cum_time[result] = time
        else:
            self.cum_time[result] = self.cum_time.get(result) + time

        # print(self.cum_time)

        # print("forbidden_activity--time--", pytz.timezone('Asia/Dhaka').localize(time))
        # print("forbidden_activity--start_time--", start_time.strftime("%Y-%m-%d %H:%M"))
        # print("forbidden_activity--end_time--", end_time.strftime("%Y-%m-%d %H:%M"))

        # time___time = pytz.timezone('Asia/Dhaka').localize(f"{time}".strftime("%Y-%m-%d %H:%M"))
        # print("forbidden_activity--time--", time.strftime("%Y-%m-%d %H:%M"))

        print("im Now Heare")
        # print(type(time))


        return activity, result, time, start_time, end_time

    def side_talk(self, image):

        distance, crop_face = self.detect.detection(image)
        times = []

        if (distance < 50):
            # print("Ready for recognition")
            start = time.time()
            # cv2.imwrite("img2.png",crop_face)
            result = self.recog.recognition(crop_face)
            # print(result)
            end = time.time()
            diff = end-start
            # print(f"Start: {start} End: {end} Diff: {diff}")
            if result not in self.cum_time.keys():
                self.cum_time[result] = diff
            else:
                self.cum_time[result] = self.cum_time.get(result) + diff

            # print(self.cum_time)

            return result, diff, start, end
        else:
            None, None, None, None

    def counters(self, image):

        name, time = self.counter.camera(image)

        return name, time

    def crop_position(self, image):

        # pts = np.array([[116,342],[904,3],[1270,29],[1234,704]])
        pts = np.array([[7, 356], [932, 17], [1127, 31], [486, 681]])
        rect = cv2.boundingRect(pts)
        x, y, w, h = rect
        croped = image[y:y+h, x:x+w].copy()
        pts = pts - pts.min(axis=0)
        mask = np.zeros(croped.shape[:2], np.uint8)
        cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
        dst = cv2.bitwise_and(croped, croped, mask=mask)

        return dst

    def main(self, image):
        # Printing the result of the function.
        # print("Merge-main------------------->",image.shape)
        image = self.crop_position(image)
        # cv2.imwrite("img2.png",image)
        # print("Merge-main------image------------->",image.shape)
        activity, for_name, time, start_time, end_time = self.forbidden_activity(image)
        
        if for_name not in self.cum_time.keys():
                self.cum_time[for_name] = time
        else:
            self.cum_time[for_name] = self.cum_time.get(for_name) + time

        # print("Merge-main------activity------------->",activity)
        # print("Merge-main------for_name------------->",for_name)
        # print("Merge-main------time------------->",time)
        # print("Merge-main------start_time------------->",start_time)
        # print("Merge-main------end_time------------->",end_time)
        # side_result, diff, start,end = self.side_talk(image)
        # print("Merge-main------side_result------------->",side_result)
        # print("Merge-main------diff------------->",diff)
        # print("Merge-main------start------------->",start)
        # print("Merge-main------end------------->",end)

        # name,total_time, loss_start, loss_end =self.counters(image)
        # print("Merge-main------name------------->",name)
        # print("Merge-main------total_time------------->",total_time)
        # print("Merge-main------loss_start------------->",loss_start)
        # print("Merge-main------loss_end------------->",loss_end)

        activity_mapping = {
            "side_talk": 1,
            "drinking": 2,
            "talking": 3,
            "eating": 4,
            "watching": 5
        }

        # data = {
        #     "forbidden_activity":
        #     {
        #         "activity": activity_mapping[activity],
        #         "name":for_name,
        #         "duration":time,
        #         "start_time":start_time,
        #         "end_time":end_time
        #     },

        #     "side_talk":
        #     {
        #         "activity": 'Side Talk',
        #         "name":side_result,
        #         "duration":diff,
        #         "start_time":start,
        #         "end_time":end
        #     },
        #     "absence":
        #     {
        #         "name":   name,
        #         "total_time":total_time,
        #         "start_time":loss_start,
        #         "end_time":loss_end
        #     }
        # }

        return {
            "activity": activity_mapping[activity],
            "name": for_name,
            "duration": time,
            "start_time": start_time,
            "end_time": end_time
        }
