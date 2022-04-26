import cv2
import numpy as np
import matplotlib.pyplot as plt
from modules import contours as con
from modules import lib_detection as ld


#wpodnet model load
wpod_net_path = "C:\\Users\\Asus\\Desktop\\Helios\\code\\ANPR\\my_version\\final_version\\model\\detection model\\wpod-net_update1.json"
wpod_net = ld.load_model(wpod_net_path)



def convertScale(img, alpha, beta):

    new_img = img * alpha + beta
    new_img[new_img < 0] = 0
    new_img[new_img > 255] = 255
    return new_img.astype(np.uint8)

# Automatic brightness and contrast optimization with optional histogram clipping
def automatic_brightness_and_contrast(image, clip_hist_percent=25):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)

    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))

    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0

    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1

    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1

    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha

    auto_result = convertScale(image, alpha=alpha, beta=beta)
    return (auto_result, alpha, beta)


#number plate detection
def detect_plate(vehicle):
#dimention size
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
        auto_result, alpha, beta = automatic_brightness_and_contrast(plate_image)
        crop_img = auto_result
        roi = plate_image

        # convert to grayscale
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(7,7),0)
        binary = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Applied inversed thresh_binary 
        thresh = cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)
        

        _, labels = cv2.connectedComponents(thresh)
        mask = np.zeros(thresh.shape, dtype="uint8")
        # Set lower bound and upper bound criteria for characters
        total_pixels = (plate_image.shape[0] * plate_image.shape[1] / 1.5)
        total_pixels2 = (plate_image.shape[1] * plate_image.shape[1])
        lower = total_pixels // 70 # heuristic param, can be fine tuned if necessary
        upper = total_pixels2 // 20 # heuristic param, can be fine tuned if necessary


        for (i, label) in enumerate(np.unique(labels)):
            # If this is the background label, ignore it
            if label == 0:
                continue
        
            # Otherwise, construct the label mask to display only connected component
            # for the current label
            labelMask = np.zeros(thresh.shape, dtype="uint8")
            labelMask[labels == label] = 255
            numPixels = cv2.countNonZero(labelMask)
        
            # If the number of pixels in the component is between lower bound and upper bound, 
            # add it to our mask
            if numPixels > lower and numPixels < upper:
                mask = cv2.add(mask, labelMask)

        # cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL)
        # cv2.imshow('finalImg', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
#transformation to detect contours
    kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thre_mor = cv2.morphologyEx(mask.copy(), cv2.MORPH_DILATE, kernel3)
    cnts, _ = cv2.findContours(thre_mor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    digit_w = 30
    digit_h = 60 


    # crop 
    test_roi = roi.copy()
    crop_digits = []


    for c in con.sort_contours(cnts):
        (x, y, w, h) = cv2.boundingRect(c)
        ratio = h/w
        if ratio<2.5: # Only select contour with defined ratio
            if (h/roi.shape[0]>=0.195):
                cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)
                curr_num = thre_mor[y:y+h,x:x+w]
                if((curr_num.shape[0]>=150) or (curr_num.shape[1]>=180)):
                    curr_num=np.delete(curr_num,c)
                else:
                    try:
                        curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h),interpolation=cv2.INTER_AREA)
                        _, curr_num = cv2.threshold(curr_num, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                        crop_digits.append(curr_num) 
                    except:
                        break 

    # cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL)
    # cv2.imshow('finalImg', test_roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite('finalImage.jpg', test_roi)
    
    return crop_digits
              