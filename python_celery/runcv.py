import cv2

cam = cv2.VideoCapture("rtsp://admin:Hik12345@192.168.1.202")

while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break