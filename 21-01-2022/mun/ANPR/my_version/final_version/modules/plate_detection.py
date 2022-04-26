import cv2
import numpy as np
import matplotlib.pyplot as plt
from modules import contours as con
from modules import lib_detection as ld



wpod_net_path = "./model/detection model/wpod-net_update1.json"
wpod_net = ld.load_model(wpod_net_path)


def detect_plate(vehicle):

    Dmax = 608
    Dmin = 288

    ratio = float(max(vehicle.shape[:2])) / min(vehicle.shape[:2])
    side = int(ratio * Dmin)
    bound_dim = min(side, Dmax)

    L , LpImg, lp_type = ld.detect_lp(wpod_net, ld.im2single(vehicle), bound_dim, lp_threshold=0.5)
    # print("Detect %i plate(s)"%len(LpImg))
    
    if (len(LpImg)):
 
        # Scales, calculates absolute values, and converts the result to 8-bit.
        plate_image = cv2.convertScaleAbs(LpImg[0], alpha=(255.0))

        roi = LpImg[0]

        # convert to grayscale
        gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(7,7),0)

        # Applied inversed thresh_binary 
        binary = cv2.threshold(blur, 180, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    thre_mor = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel3)
    cont, _  = cv2.findContours(thre_mor, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    digit_w = 30
    digit_h = 60 


    # crop 
    test_roi = roi.copy()
    crop_digits = []

    for c in con.sort_contours(cont):
        (x, y, w, h) = cv2.boundingRect(c)
        ratio = h/w
        if 1.5<=ratio<=2: # Only select contour with defined ratio
            if (h/roi.shape[0]>=0.20):
                cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)
                curr_num = thre_mor[y:y+h,x:x+w]
                curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                _, curr_num = cv2.threshold(curr_num, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                crop_digits.append(curr_num)

    # cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL)
    # cv2.imshow('finalImg', test_roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return crop_digits
              