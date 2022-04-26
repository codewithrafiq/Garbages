import os
import time
import cv2
import math
import numpy as np

class Detection:
    def __init__(self, model_path='checkpoints/facedetector/', use_gpu=True):
        caffemodel = model_path+"RetinaFace.caffemodel"
        deploy = model_path+"deploy.prototxt"
        self.detector = cv2.dnn.readNetFromCaffe(deploy, caffemodel)
        self.detector_confidence = 0.6
        if use_gpu:
            self.detector.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.detector.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
            #setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
            
            
    def get_bbox(self, img):
        height, width = img.shape[0], img.shape[1]
        aspect_ratio = width / height
        if img.shape[1] * img.shape[0] >= 192 * 192:
            img = cv2.resize(img,
                             (int(192 * math.sqrt(aspect_ratio)),
                              int(192 / math.sqrt(aspect_ratio))), interpolation=cv2.INTER_LINEAR)

        blob = cv2.dnn.blobFromImage(img, 1, mean=(104, 117, 123))
        self.detector.setInput(blob, 'data')
        
        out = self.detector.forward('detection_out').squeeze()
        max_conf_index = np.argmax(out[:, 2])
        left, top, right, bottom = out[max_conf_index, 3]*width, out[max_conf_index, 4]*height, \
                                   out[max_conf_index, 5]*width, out[max_conf_index, 6]*height
        bbox = [int(left), int(top), int(right-left+1), int(bottom-top+1)]
        return bbox
    
    
    def _get_new_box(self, src_w, src_h, bbox, scale):
        x = bbox[0]
        y = bbox[1]
        box_w = bbox[2]
        box_h = bbox[3]

        scale = min((src_h-1)/box_h, min((src_w-1)/box_w, scale))

        new_width = box_w * scale
        new_height = box_h * scale
        center_x, center_y = box_w/2+x, box_h/2+y

        left_top_x = center_x-new_width/2
        left_top_y = center_y-new_height/2
        right_bottom_x = center_x+new_width/2
        right_bottom_y = center_y+new_height/2

        if left_top_x < 0:
            right_bottom_x -= left_top_x
            left_top_x = 0

        if left_top_y < 0:
            right_bottom_y -= left_top_y
            left_top_y = 0

        if right_bottom_x > src_w-1:
            left_top_x -= right_bottom_x-src_w+1
            right_bottom_x = src_w-1

        if right_bottom_y > src_h-1:
            left_top_y -= right_bottom_y-src_h+1
            right_bottom_y = src_h-1

        return int(left_top_x), int(left_top_y),\
               int(right_bottom_x), int(right_bottom_y)
    

    def crop(self, org_img, bbox, scale, out_w, out_h, crop=True):
        if not crop:
            dst_img = cv2.resize(org_img, (out_w, out_h))
        else:
            src_h, src_w, _ = np.shape(org_img)
            left_top_x, left_top_y, \
                right_bottom_x, right_bottom_y = self._get_new_box(src_w, src_h, bbox, scale)
            
            img = org_img[left_top_y: right_bottom_y+1,
                          left_top_x: right_bottom_x+1]
            dst_img = cv2.resize(img, (out_w, out_h))
        return dst_img
    
    
    def get_cropped_face(self,image, scale=1, h_input=112, w_input=112, crop=True):
        """
        Input:
            image: should be open cv BGR image  (numpy)
            scale: for getting relux bbox
            h_input: cropped height resize to 112
            w_input: cropped width  resize to 112
            crop: get cropped image or not
        Output: 
            cropped_img: BRG image
        """

        bbox = self.get_bbox(image)
        if bbox==[0,0,1,1]:
            return None, None
        else:
            param = {
            "org_img": image,
            "bbox": bbox,
            "scale": scale,
            "out_w": w_input,
            "out_h": h_input,
            "crop": crop,
            }
            if scale is None:
                param["crop"] = False
            cropped_img = self.crop(**param)
            return cropped_img, bbox
        
