
import cv2
import numpy as np
from keras.models import model_from_json
from keras.models import Sequential


model = Sequential()
json_file = open('./model/12 class model/License_plate_v2_nvidia.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('./model/12 class model/License_plate_v2_nvidia.h5')


digit_names = ('0','1','2','3','4','5','6','7','8','9','CHA','GA')

def model_predict(image):
    global digit_names
    img = np.asarray(image,dtype=np.float32)
    img = cv2.resize(img,(80,224))
    img = img/255
    img = img[np.newaxis,:]
    if len(img.shape)<4:
        img = np.stack((img,)*3, axis=-1)
    max_value = max((model.predict(img)[0]))
    index = np.where(model.predict(img)[0]==max_value)
    return digit_names[int(index[0])]