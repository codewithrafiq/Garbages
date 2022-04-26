import cv2 as cv
import numpy as np


img = cv.imread("opencv-course/Resources/Photos/park.jpg")

# # Translation
# def translate(image, x, y):
#     M = np.float32([[1, 0, x], [0, 1, y]])
#     shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
#     return shifted
# translation__ = translate(img, -100, 50)



# # Rotation
# def rotate(img,angle,rotPoint=None):
#     (h,w) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (w/2,h/2)
#     M = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     rotated = cv.warpAffine(img,M,(w,h))
#     return rotated

# rotated = rotate(img,45)


# cv.imshow("Shifted", rotate(rotated,-0))









cv.waitKey(0)