import cv2
import numpy as np
import time
import datetime

class FORBIDDEN_ACTIVITY:

    def __init__(self):

        self.net1 = cv2.dnn.readNet('project/ml/yolo/model/forbidden_activity.weights','project/ml/yolo/model/forbidden_activity.cfg')
        # self.net1.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # self.net1.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        global start
        self.classes=[]

        with open('project/ml/yolo/model/forbidden_activity.names', 'r') as f:
            self.classes = f.read().splitlines()

        self.net2 = cv2.dnn.readNet('project/ml/yolo/model/forbidden_activity.weights','project/ml/yolo/model/forbidden_activity.cfg')
        # self.net2.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # self.net2.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        global start
        self.classes2=[]

        with open('project/ml/yolo/model/forbidden_activity.names', 'r') as f:
            self.classes2 = f.read().splitlines()


    def activity(self, img):
        
        # img=self.person(image)
        # print(img.shape)
        # cv2.imshow("frame",img)
        # global end
        
        height, width, _ = img.shape
        blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
 
        self.net1.setInput(blob)
        output_layers_names = self.net1.getUnconnectedOutLayersNames()
        
        layerOutputs = self.net1.forward(output_layers_names)
        
        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)

                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)


        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        total_time=[]
        try:
            if len(indexes) > 0:
                for i in indexes.flatten():
                    x, y, w, h = boxes[i]
                    label =  str(self.classes[class_ids[i]])
                    #print(label)
                    if(label == 'drinking') or (label =="talking") or (label == 'watching') or (label =="eating"):
                        start=datetime.datetime.now()
                        crop_image=img[y:y+h,x:x+w]
                        # cv2.imwrite("crop_image.jpg",crop_image)
                        # print(crop_image)
                        # cv2.imshow('crop',crop_image)
                        object_label=self.object(crop_image)
                        # print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",label,object_label)
                        #if(label != label):
                        end=datetime.datetime.now()

                        #print(label)
                        time_diff=end-start
                        total_time.append(time_diff)
                        non_activity_time=np.array(total_time)
                        non_activity_time=non_activity_time.sum()
                        # print(non_activity_time)

                        # print("crope----image",crop_image.shape)
                print("label,non_activity_time,crop_image, start,end",label,non_activity_time,crop_image.shape, start,end)
                return label,non_activity_time,crop_image, start,end
                
        except Exception as e :
            print(e)
            pass
            



    def object(self, img):
        height, width, _ = img.shape
        blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
        self.net1.setInput(blob)
        output_layers_names = self.net1.getUnconnectedOutLayersNames()
        layerOutputs = self.net1.forward(output_layers_names)
        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)

                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)
      

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        try:
            if len(indexes) > 0:
                for i in indexes.flatten():
                    x, y, w, h = boxes[i]
                    label =  str(self.classes[class_ids[i]])
                
                    if(label == 'bottle'):

                        return label

                    else:
                        return "no_object"

        except Exception as e:
            pass
        
        
    def person(self, img):
        height, width, _ = img.shape
        blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
        self.net2.setInput(blob)
        output_layers_names = self.net2.getUnconnectedOutLayersNames()
        layerOutputs = self.net2.forward(output_layers_names)
        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)

                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)
      
        # print(len(boxes))
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        try:
            if len(indexes) > 0:
                for i in indexes.flatten():
                    x, y, w, h = boxes[i]
                    label =  str(self.classes2[class_ids[i]])
                    crop_image=img[y:y+h,x:x+w]
                    
                    return crop_image
                


        except Exception as e:
            pass

    
  






                

