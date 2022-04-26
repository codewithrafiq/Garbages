import cv2 as cv
import numpy as np


# img = cv.imread("opencv-course/Resources/Photos/cat.jpg")
# cv.imshow("Cat",img)




blank = np.zeros((512,512,3),dtype=np.uint8)
blank[:]=0,255,0
blank[200:300,400:500] = 0,0,255

cv.rectangle(blank,(100,100),(300,300),(255,0,0),thickness=3)
cv.circle(blank,(200,200),100,(0,0,255),thickness=3)
cv.line(blank,(0,0),(511,511),(255,255,255),thickness=3)
cv.putText(blank,"Hello World",(100,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,115,0),thickness=3)

cv.imshow("Blank",blank)
cv.waitKey(0)