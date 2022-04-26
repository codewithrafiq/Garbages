from threading import Thread
import cv2
import numpy as np





class VideoGet:

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True



# class VideoProses:
#     def __init__(self, frame):
#         self.frame = frame

#     def start(self):
#         Thread(target=self.show, args=()).start()
#         return self
    
#     def show(self):
#         cascPath = 'haarcascade_frontalface_dataset.xml'
#         faceCascade = cv2.CascadeClassifier(cascPath)
#         while True:
#             gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
#             faces = faceCascade.detectMultiScale(
#                 gray,
#                 scaleFactor=1.1,
#                 minNeighbors=5,
#                 minSize=(30, 30),
#                 flags=cv2.CASCADE_SCALE_IMAGE
#             )
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             self.frame = self.frame

net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()
    
class VideoProses:
    def __init__(self, frame):
        self.frame = frame

    def start(self):
        Thread(target=self.show, args=()).start()
        return self
    
    def show(self):
        while True:
            height, width, _ = self.frame.shape
            blob= cv2.dnn.blobFromImage(self.frame, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
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
                        cv2.rectangle(self.frame, (x, y), (x+w, y+h), color, 2)
                        cv2.putText(self.frame, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)
                        print(label)
                        if label == 'person':
                            person += 1
                    print(person,"----------------")
            except:
                pass
            self.frame = self.frame


class VideoShow:
    def __init__(self, frame):
        self.frame = frame

    def start(self):
        Thread(target=self.show, args=()).start()
        return self
    
    def show(self):
        self.frame = self.frame


def threadBoth(source=0):

    video_getter = VideoGet(source).start()
    video_proses = VideoProses(video_getter.frame).start()
    video_show = VideoShow(video_proses.frame).start()
    while True:
        if video_getter.stopped:
            video_show.stop()
            break
        frame = video_getter.frame
        video_proses.frame = frame
        video_show.frame = frame
        
        if cv2.waitKey(1) == ord("q"):
            break
        cv2.imshow("Video", video_show.frame)
        
        # frame, buffer = cv2.imencode('.jpg', video_show.frame)
        # frame = buffer.tobytes()
        # yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':
    run = True
    threadBoth()