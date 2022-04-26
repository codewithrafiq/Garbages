import cv2 as cv

img = cv.imread("opencv-course/Resources/Photos/park.jpg")



# # Converting to grayscale
# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # Blurring
# blur = cv.blur(img,(3,3),cv.BORDER_DEFAULT)

# # Edge Cascade
# img = cv.Canny(img,100,200)

# # Resizing
# img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

# Cropping
img = img[50:200,200:400]

cv.imshow("Image",img)
cv.waitKey(0)
