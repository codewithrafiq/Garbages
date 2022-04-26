import face_recognition
from face_recognition.api import face_distance
import numpy as np
import cv2


# # section 1 ------------------------------------------------------------------------------------------------------------

# image1 = face_recognition.load_image_file("img/known/Elon Musk.jpg")
# image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)


# face1 = face_recognition.face_locations(image1)[0]
# encodeFace = face_recognition.face_encodings(image1)[0]

# print(len(encodeFace))

# cv2.rectangle(image1,(face1[3],face1[0]),(face1[1],face1[2]),(255,0,0),2)

# cv2.imshow("image",image1)
# cv2.waitKey(0)


# # section 2 ------------------------------------------------------------------------------------------------------------

# img1 = face_recognition.load_image_file("img/known/Elon Musk.jpg")
# ecvode1 = face_recognition.face_encodings(img1)[0]

# img2 = face_recognition.load_image_file("img/known/Barack Obama.jpg")
# ecvode2 = face_recognition.face_encodings(img2)[0]

# ressult = face_recognition.compare_faces([ecvode1,ecvode2],ecvode1)
# print(ressult)

# faceDis = face_recognition.face_distance([ecvode1,ecvode2],ecvode1)
# print(faceDis)


# # section 3 ------------------------------------------------------------------------------------------------------------


# img = cv2.VideoCapture(0)
# while True:
#     ret, frame = img.read()
#     if ret == False:
#         continue
#     try:
#         face1 = face_recognition.face_locations(frame)
#         for (top, right, bottom, left) in face1:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#     except:
#         pass
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# img.release()
# cv2.destroyAllWindows()


## section 4 ------------------------------------------------------------------------------------------------------------


# while True:
#     success, img = cap.read()
#     if not success:
#         continue
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(d, encodeFace)
#         faceDis = face_recognition.face_distance(d, encodeFace)
#         # print(faceDis)
#         matchIndex = np.argmin(faceDis)

#         if matches[matchIndex]:
#             name = classNames[matchIndex]
#             print(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

#     cv2.imshow("Face Recognizer", img)
#     cv2.waitKey(1)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break