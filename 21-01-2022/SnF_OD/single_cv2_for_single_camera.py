import cv2
# import numba
# from numba import cuda, vectorize, jit
import numpy as np
import random
import redis

net1 = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

def camera_1(index):
        cap = cv2.VideoCapture(index)
        while True:
            _, img = cap.read()
            height, width, _ = img.shape
            blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
            net1.setInput(blob)
            output_layers_names = net1.getUnconnectedOutLayersNames()
            layerOutputs = net1.forward(output_layers_names)

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
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(boxes),3))
            try:
                person = 0
                if len(indexes) > 0:
                    for i in indexes.flatten():
                        x, y, w, h = boxes[i]
                        label =  str(classes[class_ids[i]])
                        confidence = str(round(confidences[i], 2))
                        color = colors[i]
                        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                        cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
                        print(label)
                        if label == 'person':
                            person += 1
                    print(person)
            except:
                pass

            
            if img is None:
                continue
            else:
                img, buffer = cv2.imencode('.jpg', img)
                img = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')




net2 = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()
def camera_2(index):
        cap = cv2.VideoCapture(index)
        while True:
            _, img = cap.read()
            height, width, _ = img.shape
            blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
            net2.setInput(blob)
            output_layers_names = net2.getUnconnectedOutLayersNames()
            layerOutputs = net2.forward(output_layers_names)

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
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(boxes),3))
            try:
                person = 0
                if len(indexes) > 0:
                    for i in indexes.flatten():
                        x, y, w, h = boxes[i]
                        label =  str(classes[class_ids[i]])
                        confidence = str(round(confidences[i], 2))
                        color = colors[i]
                        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                        cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
                        print(label)
                        if label == 'person':
                            person += 1
                    print(person)
            except:
                pass

            
            if img is None:
                continue
            else:
                img, buffer = cv2.imencode('.jpg', img)
                img = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

net3 = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()
def camera_3(index):
        cap = cv2.VideoCapture(index)
        while True:
            _, img = cap.read()
            height, width, _ = img.shape
            blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
            net3.setInput(blob)
            output_layers_names = net3.getUnconnectedOutLayersNames()
            layerOutputs = net3.forward(output_layers_names)

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
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(boxes),3))
            try:
                person = 0
                if len(indexes) > 0:
                    for i in indexes.flatten():
                        x, y, w, h = boxes[i]
                        label =  str(classes[class_ids[i]])
                        confidence = str(round(confidences[i], 2))
                        color = colors[i]
                        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                        cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
                        print(label)
                        if label == 'person':
                            person += 1
                    print(person)
            except:
                pass

            
            if img is None:
                continue
            else:
                img, buffer = cv2.imencode('.jpg', img)
                img = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

