import face_recognition
from PIL import Image, ImageDraw



imgage_of_bill = face_recognition.load_image_file("img/known/Bill Gates.jpg")
bill_face_encoding = face_recognition.face_encodings(imgage_of_bill)[0]



image_of_steve = face_recognition.load_image_file("img/known/Steve Jobs.jpg")
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]



known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_name = [
    "Bill Gates",
    "Steve Jobs"
]


test_image = face_recognition.load_image_file("img/groups/bill-steve-elon.jpg")
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)


pil_image = Image.fromarray(test_image)

drow = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_name[first_match_index]

    drow.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
    drow.text((left + 6, bottom - 6), name, fill=(255, 255, 255, 255))



del drow


pil_image.show()