import cv2
from merge import MERGE
from vidgear.gears import VideoGear, CamGear

face = MERGE()
# detect = Detector()

# activ = FA()

# cap = cv2.VideoCapture("vi.mp4")
cap = VideoGear(source="/home/rafiq/AlterSense/Helios_G/ml_microservices/forbidden_activity_ml_model/project/ml/vi.mp4").start()

# /home/sana/Videos/office_project/merge/side_talk/models/onnx/centerface.onnx
while True:
    frame = cap.read()
    # print(frame.shape)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    try:
        # print("lllllllllllllllllllllllllllllllllllllllllll",frame)
        # distance = face.side_talk(frame)
        # print("########################################3",distance)

        # print("FFFFFFFFFFF",crop_face)
        # activity, time, image =
        a, b = face.counters(frame)
        # print("###############", a)
        # print("###############",b)
        # print("###############",c)
        # print("###############",d)
        # print("###############",e)

        # cv2.imwrite("img.png",image)
        # if activity == "Drinking" or "Talking":
        #     data = face.face_recognition(frame)
        #     print("ffffffffffffffrrrrrrrrrrrrrrrr",data)
        # else:
        #     continue
        # print("WWWWWWWWWWWWWWWWWWWWWWWW", activity, time)
    except:
        continue

    # cv2.imshow('Webcam',frame)
    # # cv2.imshow('Webcam',image)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cv2.destroyAllWindows()
