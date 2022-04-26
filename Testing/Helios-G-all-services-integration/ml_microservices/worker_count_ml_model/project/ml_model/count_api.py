from project.ml_model.src.persondetection import TrackableObject, CentroidTracker, DetectorAPI
import cv2
import numpy as np
import datetime
import pytz


class COUNTING:
    def __init__(self):

        self.odapi = DetectorAPI()
        self.threshold = 0.7
        self.ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
        self.trackableObjects = {}
        self.DHK = pytz.timezone('Asia/Dhaka')

    def entry_count(self, frame):

        totalDown = 0
        totalUp = 0
        img = cv2.resize(frame, (800, 720))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        frameHeight = img.shape[0]
        frameWidth = img.shape[1]
        line_up = int(2*(frameHeight/2.2))
        line_down = int(3*(frameHeight/3.5))
        # print(line_down)
        boxes, scores, classes, num = self.odapi.processFrame(img)
       # print("..........boxes......>>>>>>>>>",boxes)
        pts = np.array([[180, 150],
                        [410, 160],
                        [800, 550]],
                       np.int32)
        rect = []
        for i in range(len(boxes)):

            if classes[i] == 1 and scores[i] > self.threshold:
                box = boxes[i]
                rect.append((box[1], box[0], box[3], box[2]))
                # cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,0),2)

        objects = self.ct.update(rect)
        for (objectID, centroid) in objects.items():
            to = self.trackableObjects.get(objectID, None)
            if to is None:
                to = TrackableObject(objectID, centroid)
            else:
                y = [c[1] for c in to.centroids]
                # print("..........y......>>>>>>>>>",np.mean(y))
                # print("...........centroid[1].....>>>>>>>>>", centroid[1])
                direction = centroid[1] - np.mean(y)
                # print("---------direction-------...>>>>>>>>>", direction)
                to.centroids.append(centroid)
                if not to.counted:

                    if direction < 0:

                        if centroid[1] in range(283, 531):
                            totalUp += 1
                            to.counted = True
                        else:
                            continue

                        # if direction < 0 and centroid[1] < line_up:
                        #     totalUp += 1
                        #     to.counted = True

                    elif direction > 0:

                        if centroid[1] in range(293, 531):
                            totalDown += 1
                            to.counted = True
                        else:
                            continue

                    # if direction < 0 :
                    #     if 0<centroid[1]-460<80:
                    #         totalUp += 1
                    #         to.counted = True
                    #     else:
                    #         continue

                    # elif direction > 0 :
                    #     if   -70<centroid[1]-460<0:
                    #         totalDown += 1
                    #         to.counted = True
                    #     else:
                    #         continue
            self.trackableObjects[objectID] = to
        info = [
            ("Up", totalUp),
            ("Down", totalDown),
        ]
        # print("--------------------------------------.......>>>>>>>>>>>>", info)
        result = {
            "enter": totalDown,
            "time": f'{datetime.datetime.now(self.DHK).strftime("%Y-%m-%d %H:%M")}',
            "exit": totalUp
        }
        return result

    # def exit_count(self, frame):
    #     totalDown = 0
    #     totalUp = 0
    #     img = cv2.resize(frame, (800, 600))
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #     frameHeight = img.shape[0]
    #     frameWidth = img.shape[1]

    #     line_up = int(2*(frameHeight/2.2))
    #     line_down = int(3*(frameHeight/3.5))

    #     boxes, scores, classes, num = self.odapi.processFrame(img)

    #     pts = np.array([[180, 150],
    #                     [410, 160],
    #                     [800, 550]],
    #                    np.int32)
    #     rect = []

    #     for i in range(len(boxes)):

    #         if classes[i] == 1 and scores[i] > self.threshold:
    #             box = boxes[i]
    #             rect.append((box[1], box[0], box[3], box[2]))
    #             cv2.rectangle(img, (box[1], box[0]),
    #                           (box[3], box[2]), (255, 0, 0), 2)

    #     objects = self.ct.update(rect)

    #     for (objectID, centroid) in objects.items():
    #         to = self.trackableObjects.get(objectID, None)

    #         if to is None:
    #             to = TrackableObject(objectID, centroid)

    #         else:
    #             y = [c[1] for c in to.centroids]
    #             # print("..........y......>>>>>>>>>",np.mean(y))
    #             # print("...........centroid[1].....>>>>>>>>>",centroid[1])
    #             direction = centroid[1] - np.mean(y)
    #             # print("---------direction-------...>>>>>>>>>",direction)
    #             to.centroids.append(centroid)

    #             if not to.counted:

    #                 if direction < 0:
    #                     if 0 < centroid[1]-293 < 80:
    #                         totalUp += 1
    #                         to.counted = True
    #                     else:
    #                         continue

    #                 elif direction > 0:
    #                     if -70 < centroid[1]-460 < 0:
    #                         totalDown += 1
    #                         to.counted = True
    #                     else:
    #                         continue

    #         self.trackableObjects[objectID] = to

    #     info = [
    #         ("Up", totalUp),
    #         ("Down", totalDown),
    #     ]
    #     print("--------------------------------------.......>>>>>>>>>>>>", info)
    #     # print("Up", self.totalUp)
    #     # print("Down", self.totalDown)

    #     result = {"exit": totalUp,
    #               "time": datetime.datetime.now().timestamp()}

    #     return result

    # def entry_count(self, img):

    #     odapi = DetectorAPI()
    #     threshold = 0.7
    #     ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
    #     trackableObjects = {}
    #     totalUp = 0
    #     totalDown = 0
    #     img = cv2.resize(img, (800, 720))
    #     print(img)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     # print(img.shape)
    #     frameHeight = img.shape[0]
    #     frameWidth = img.shape[1]
    #     boxes, scores, classes, num = odapi.processFrame(img)
    #     print(boxes)
    #     pts = np.array([[180,150],
    #                 [410, 160],
    #                 [800, 550]],
    #                 np.int32)
    #     rect= []

    #     for i in range(len(boxes)):

    #         if classes[i] == 1 and scores[i] > threshold:
    #             box = boxes[i]
    #             rect.append((box[1],box[0],box[3],box[2]))
    #             cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,0),2)

    #     objects  =ct.update(rect)

    #     for (objectID, centroid) in objects.items():
    #         to = trackableObjects.get(objectID, None)

    #         if to is None:
    #             to = TrackableObject(objectID, centroid)

    #         else:
    #             y = [c[1] for c in to.centroids]
    #             print("..........y......>>>>>>>>>",np.mean(y))
    #             print("...........centroid[1].....>>>>>>>>>",centroid[1])
    #             direction = centroid[1] - np.mean(y)
    #             print("---------direction-------...>>>>>>>>>",direction)
    #             to.centroids.append(centroid)

    #             if not to.counted:

    #                 if direction < 0 :
    #                     if -20<= (centroid[1]-460) <=0:
    #                         totalUp += 1
    #                         to.counted = True
    #                     else:
    #                         continue

    #                 # if direction < 0 and centroid[1] < line_up:
    #                 #     totalUp += 1
    #                 #     to.counted = True

    #                 elif direction > 0 :

    #                     if  0 < centroid[1]-460 < 50:
    #                         totalDown += 1
    #                         to.counted = True
    #                     else:
    #                         continue
    #         trackableObjects[objectID] = to

    #         cv2.circle(img, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

    #     info = [
    #         ("Up", totalUp),
    #         ("Down", totalDown),
    #         ]
    #     print("Up", totalUp)
    #     print("Down", totalDown)

    #     # for (i, (k, v)) in enumerate(info):
    #     #     text = "{}: {}".format(k, v)
    #     #     cv2.putText(img, text, (10, frameHeight - ((i * 20) + 20)),
    #     #         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    #     #img = cv2.polylines(img,[pts_L1],False,line_down_color,thickness=2)
    # # cv2.line(img, (0, line_down),(frameWidth, line_down), (0, 0, 0), 3)

    #     # img = cv2.polylines(img, [pts],False,  (255, 240, 0), thickness=2)

    #     # cv2.imshow("preview", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
