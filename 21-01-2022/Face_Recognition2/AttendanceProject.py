import cv2
import face_recognition
import os
import numpy as np


path = "img/known/"
images = []
classNames = []

myList = os.listdir(path)
for cls in myList:
    curImg = cv2.imread(f'{path}{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

print(classNames)

def findEncoding(images):
    encodeList = []
    for img in images:
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
    return encodeList

encodeListKnown = findEncoding(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    facesFurFrame = face_recognition.face_locations(imgS)
    encodesFurFrame = face_recognition.face_encodings(imgS, facesFurFrame)

    for encodeFace, faceLoc in zip(encodesFurFrame, facesFurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        # print(matches)
        matchIndex = np.argmin(faceDis)
        # print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex]
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    cv2.imshow("Face", img)
    cv2.waitKey(1)