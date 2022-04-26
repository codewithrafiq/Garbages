import cv2
import numba
from numba import cuda, vectorize, jit
import numpy as np

#print(cuda.gpus)

net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()


#img = cv2.imread('iamge.jpg') #INPUT IMAGE HERE
#@vectorize(['float64(float64)'], target ="cuda")
#@numba.jit(target='cuda')
#@jit
def objectify(cap):
    while True:
        _, img = cap.read()
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
        key = cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
rtsp_username = "admin"
rtsp_password = "abc12345"
width = 800
height = 480
cam_no = 1

def create_camera (channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@119.148.38.194:554/Streaming/channels/" + channel + "01" #change the IP to suit
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 640) # ID number for width is 3
    cap.set(4, 480) # ID number for height is 480
    cap.set(10, 100) # ID number for brightness is 10qq
    return cap
cam = create_camera(str(cam_no))
objectify(cam)

