import cv2 as cv
import numpy as np

img = cv.imread("./opencv-course/Resources/Photos/cats.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(gray, 50, 150)
# canny = cv.Canny(blur, 125, 175)

# cv.imshow("Canny", canny)

ret,thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print("Number of contours found: ", len(contours))


cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Contours", blank)


cv.waitKey(0)