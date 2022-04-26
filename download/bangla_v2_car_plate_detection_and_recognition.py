
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#tensorflow warning message hide
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
try:
    from tensorflow.python.util import module_wrapper as deprecation
except ImportError:
    from tensorflow.python.util import deprecation_wrapper as deprecation
deprecation._PER_MODULE_WARNING_LIMIT = 0

#library import
import cv2
import numpy as np
import matplotlib.pyplot as plt

#module import
from modules import digit_recognition as dr
from modules import plate_detection as pd

#number plate recognition
def plate_recognition(vehicle):
 #number plate detection from plate detection

    crop_digits=pd.detect_plate(vehicle)

    fig = plt.figure(figsize=(8,5))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)      

    col = len(crop_digits)
    row = 1

    final_result = []
    #crop digit from number plate
    for digit in crop_digits:
        # fig.add_subplot(1,col,row)
        title = dr.model_predict(digit)
        final_result.append(title)
        row+=1   


    for index, value in enumerate(final_result):
      if (value == 'GA') or (value == 'CHA'):
        final_result.pop(index)
        final_result.insert(0,value)

    listToStr = ' '.join([str(elem) for elem in final_result]) 
    print("Recognize Number Plate:",listToStr) 




    final_image = cv2.copyMakeBorder(src=vehicle,top=0,bottom=200,left=0,right=0,
                                    borderType=cv2.BORDER_CONSTANT, value=[255,255,255])
    h,w = final_image.shape[:2]
    # cv2.putText(final_image,listToStr,(int(w/2-170),int(h-80)),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),5,cv2.LINE_AA)
    # cv2.namedWindow('finalImg', cv2.WINDOW_NORMAL) 
    # cv2.imshow('finalImg',final_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return listToStr


# vehicle_image = plt.imread("C:\\Users\\Asus\\Desktop\\Helios\\code\\ANPR\\my_version\\final_version\\test data\\TEST1 (3).jpg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("my_version/final_version/test data/picup.jpeg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\shdw.JPG")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\side.JPG")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\small.jpg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\syl.jpg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\wnb.JPG")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\1.jpg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\2.jpg")
# plate_recognition(vehicle_image)

# vehicle_image = plt.imread("test data\\3.jpg")
# plate_recognition(vehicle_image)



