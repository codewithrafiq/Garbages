import cv2
import cv2
import numba
from numba import cuda, vectorize, jit
import numpy as np
import random
import redis


redis_client = redis.Redis(host='localhost', port=6379)




def gen_frames(index=0):
        vs = cv2.VideoCapture(index)
        while True:
            ret, frame = vs.read()
            if frame is None:
                continue
            else:
                img_str1 = cv2.imencode('.jpg', frame)[1].tostring()
                key = random.randint(0, 999999999999999999999999999)
                redis_client.set(key, img_str1,ex=1)
                img_str2 = redis_client.get(key)
                img_np = cv2.imdecode(np.frombuffer(img_str2, np.uint8), 1)

                frame, buffer = cv2.imencode('.jpg', img_np)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')











net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

class SingleThreadedStreamingYolov3:

    def __init__(self, index=0):
        self.cap = cv2.VideoCapture(index)
        self.data = []


    def objectify(self):
        while True:
            _, img = self.cap.read()
            height, width, _ = img.shape
            blob= cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
            net.setInput(blob)
            output_layers_names = net.getUnconnectedOutLayersNames()
            layerOutputs = net.forward(output_layers_names)

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
                img_str1 = cv2.imencode('.jpg', img)[1].tostring()
                key = random.randint(0, 999999999999999999999999999)
                redis_client.set(key, img_str1,ex=1)
                img_str2 = redis_client.get(key)
                img_np = cv2.imdecode(np.frombuffer(img_str2, np.uint8), 1)


                img, buffer = cv2.imencode('.jpg', img_np)
                img = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

