import cv2
import numpy as np
import threading


net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()


def objectify(source):
    while True:
        _, img = cv2.VideoCapture(source).read()
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

        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label =  str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)

        cv2.imshow('Image', img)
        cv2.waitKey(1)




def single_threaded_for_single_camera(source,name):
    name = threading.Thread(target=objectify, args=(source,))
    print(name)
    name.start()
    name.join()


if __name__ == '__main__':
    single_threaded_for_single_camera(0,"t1")
    single_threaded_for_single_camera(2,"t2")