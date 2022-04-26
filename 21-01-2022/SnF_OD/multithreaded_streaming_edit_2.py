import cv2
import numpy as np
import threading


net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()


class VideoFeed:
    """
       this module is return Single threading for single camera
    """
    def __init__(self,camera_id,thread="thread"):
        self.cap = cv2.VideoCapture(camera_id)
        self.frame = None
        self.stopped = False
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def update(self):
        while True:
            if self.stopped:
                return
            if not self.cap.isOpened():
                self.cap.open()
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
            else:
                self.cap.release()
                self.cap.open()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.thread.join()
        self.cap.release()

if __name__ == "__main__":
    v1 = VideoFeed(0,"thread1")
    while True:
        frame = v1.read()
        cv2.imshow("frame",frame)