from src.persondetection import TrackableObject,CentroidTracker,DetectorAPI
import cv2
import numpy as np
import tensorflow as tf
from vidgear.gears import VideoGear

# import onnxruntime as rt
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

# def brightness(img):
#     lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#     l, a, b = cv2.split(lab)
#     clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
#     cl = clahe.apply(l)
#     limg = cv2.merge((cl,a,b))
#     final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

#     return final


# def distance(input_value):

#     for i in range(input_value, input_value+600):
#         x =i
#     return x
        

# print(distance(100))

if __name__ == "__main__":
    
    path="rtsp://admin:Admin2020@202.74.243.147:554/trackID=5"
    # path="video_00005.mp4"
    # path="0"
    odapi = DetectorAPI()
    threshold = 0.7
    cap = VideoGear(source=path).start()
    
    ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
    trackableObjects = {}
    
    h = 440
    w = 590


    line_up = int(2*(h/2.2))
    line_down =int(3*(h/3.5))    
    up_limit = int(1*(h/1.1))
    down_limit = int(4*(h/5))
    
    line_down_color = (255,0,0)
    line_up_color = (0,0,255)
    pt1 =  [0, line_down];
    pt2 =  [w, line_down];
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))
    pt3 =  [0, line_up];
    pt4 =  [w, line_up];
    pts_L2 = np.array([pt3,pt4], np.int32)
    pts_L2 = pts_L2.reshape((-1,1,2))
    
    pt5 =  [0, up_limit];
    pt6 =  [w, up_limit];
    pts_L3 = np.array([pt5,pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1,1,2))
    pt7 =  [0, down_limit];
    pt8 =  [w, down_limit];
    pts_L4 = np.array([pt7,pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1,1,2))

    font = cv2.FONT_HERSHEY_SIMPLEX
  
  
    totalDown=0
    totalUp =0
    
    while True:
        img1 = cap.read()
        img = cv2.resize(img1, (800, 720))
        # img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
        # img = brightness(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(img.shape)
        frameHeight = img.shape[0]
        frameWidth = img.shape[1]
        boxes, scores, classes, num = odapi.processFrame(img)

#         img_data = np.expand_dims(img.astype(np.uint8), axis=0)
#         sess = rt.InferenceSession("t.onnx")

# # # we want the outputs in this order
#         outputs = ["num_detections:0", "detection_boxes:0", "detection_scores:0", "detection_classes:0"]
#         result = sess.run(outputs, {"image_tensor:0": img_data})
#         num, boxes, scores, classes = result
#         print(len(scores))
        pts = np.array([[180,150],  
                    [410, 160],
                    [800, 550]], 
                   np.int32)       
        rect= []
        
        for i in range(len(boxes)):

            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                rect.append((box[1],box[0],box[3],box[2]))
                cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,0),2)
                
             
        objects  =ct.update(rect)        
       
        for (objectID, centroid) in objects.items():
            to = trackableObjects.get(objectID, None)
     
            if to is None:
                to = TrackableObject(objectID, centroid)
     
            else:
                y = [c[1] for c in to.centroids]
                # print("..........y......>>>>>>>>>",np.mean(y))
                # print("...........centroid[1].....>>>>>>>>>",centroid[1])
                direction = centroid[1] - np.mean(y)
                # print("---------direction-------...>>>>>>>>>",direction)
                to.centroids.append(centroid)
     
                if not to.counted:

                    # if direction < 0 :

                    #     if -20<= (centroid[1]-353) <=0:
                    #         totalUp += 1
                    #         to.counted = True
                    #     else:
                    #         continue
                    
                    # # if direction < 0 and centroid[1] < line_up:
                    # #     totalUp += 1
                    # #     to.counted = True
     
                    # elif direction > 0 :

                    #     if  0 < centroid[1]-353 < 50:
                    #         totalDown += 1
                    #         to.counted = True
                    #     else:
                    #         continue
                    if direction < 0 :
                       
                        
                        if centroid[1] in range(283, 531):
                            totalUp += 1
                            to.counted = True
                        else:
                            continue
                        
                        # if direction < 0 and centroid[1] < line_up:
                        #     totalUp += 1
                        #     to.counted = True
        
                    elif direction > 0 :

                        if centroid[1] in range(293, 531):
                            totalDown += 1
                            to.counted = True
                        else:
                            continue

            trackableObjects[objectID] = to

            cv2.circle(img, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
        

        info = [
            ("Up", totalUp),
            ("Down", totalDown),
            ]
        # print("Exit", totalUp)
        # print("Entry", totalDown)

        # for (i, (k, v)) in enumerate(info):
        #     text = "{}: {}".format(k, v)
        #     cv2.putText(img, text, (10, frameHeight - ((i * 20) + 20)),
        #         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            
        
        #img = cv2.polylines(img,[pts_L1],False,line_down_color,thickness=2)
        cv2.line(img, (191, 290),(494, 716), (230,255, 0), 3)
        # cv2.line(img, (0, 364),(frameWidth, 364), (230, 230, 0), 3)
        # cv2.line(img, (0, 295),(frameWidth, 295), (230, 0, 0), 3)
        # cv2.line(img, (0, 463),(frameWidth, 463), (230, 0, 0), 3)
        # img = cv2.polylines(img, [pts],False,  (255, 240, 0), thickness=2)
              

        cv2.imshow("preview", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break


# def enrty_count(self, img):
#     totalUp = 0
#     totalDown = 0
#     img = cv2.resize(img1, (800, 720))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # print(img.shape)
#     frameHeight = img.shape[0]
#     frameWidth = img.shape[1]
#     boxes, scores, classes, num = odapi.processFrame(img)

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
#             # print("..........y......>>>>>>>>>",np.mean(y))
#             # print("...........centroid[1].....>>>>>>>>>",centroid[1])
#             direction = centroid[1] - np.mean(y)
#             # print("---------direction-------...>>>>>>>>>",direction)
#             to.centroids.append(centroid)
    
#             if not to.counted:

#                 if direction < 0 :
#                     if -20<= (centroid[1]-line_down) <=0:
#                         totalUp += 1
#                         to.counted = True
#                     else:
#                         continue
                
#                 # if direction < 0 and centroid[1] < line_up:
#                 #     totalUp += 1
#                 #     to.counted = True
    
#                 elif direction > 0 :

#                     if  0 < centroid[1]-line_down < 50:
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
#     cv2.line(img, (0, line_down),(frameWidth, line_down), (0, 0, 0), 3)
    
#     # img = cv2.polylines(img, [pts],False,  (255, 240, 0), thickness=2)
            

#     cv2.imshow("preview", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


    

