import cv2 as cv


img = cv.imread("opencv-course/Resources/Photos/cat_large.jpg")


def rescaleFram(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)  

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# f_img = rescaleFram(img,scale=0.2)
# cv.imshow("Cat",f_img)
# cv.waitKey(0)



# capture = cv.VideoCapture("opencv-course/Resources/Videos/dog.mp4")
capture = cv.VideoCapture(0)

def chaneRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue,feame = capture.read()

    frame_resized = rescaleFram(feame,scale=0.2)


    cv.imshow("Video",frame_resized)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()