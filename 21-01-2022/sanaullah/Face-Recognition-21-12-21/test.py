from beckhend.main.face_api_video import RECOG
from beckhend.embed_save import SAVE_EMBDED
import cv2

recog =RECOG()



cap=cv2.VideoCapture(0)
while True:
    _,f=cap.read()
    try:
        r = recog.recognition(f)
    # print("rrrrrrrrrrrrr",r)
    except:
        continue
    cv2.imshow("V",r)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# from embed_save import SAVE_EMBDED


# save = SAVE_EMBDED()

# path = "./data/"


# train=save.save_multiple_embed(path)
# # import pickle


# # with open('./embds_dict_ad.pkl', 'rb') as handle:
# #     b = pickle.load(handle)
# #     print(b)
