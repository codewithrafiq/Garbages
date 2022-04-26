import face_recognition

image = face_recognition.load_image_file("img/groups/team2.jpg")
face_locations = face_recognition.face_locations(image)



print(face_locations)
print("Found {} faces in the image.".format(len(face_locations)))