import os
import cv2
import time
from beckhend.main import utils
import pickle
import datetime
import numpy as np
import tensorflow as tf
from beckhend.mtcnn.MTCNN import DetectionMtcnn
from beckhend.src.modules.models import ArcFaceModel
from scipy.spatial.distance import euclidean
from beckhend.src.modules.utils import set_memory_growth, load_yaml, l2_norm


def load_pickle(path):
    file = open(path,'rb')
    embedding = pickle.load(file)
    name =[]
    for i in embedding.keys():
        name.append(i)
    return name, embedding


class RECOG:
    def __init__(self):
        self.path =os.getcwd()
        self. detector = DetectionMtcnn()
        self.embed = "./embds_dict_ad.pkl"
        self.input_size = 112
        self.backbone_type = 'ResNet50'
        self.sub_name = 'arc_res50'
        self.model = ArcFaceModel(size=self.input_size,
                         backbone_type=self.backbone_type,
                         training=False)
        self.ckpt_path = tf.train.latest_checkpoint(self.path+'/checkpoints/' + self.sub_name)

        if self.ckpt_path is not None:
            print("[*] load ckpt from {}".format(self.ckpt_path))
            self.model.load_weights(self.ckpt_path)
        else:
            print("[*] Cannot find ckpt from {}.".format(self.ckpt_path))
            exit()
        
        self.name, self.embedding = load_pickle(self.embed)


    def recognition(self,image):
        

        faces = image
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
        faces, bbox,landmarks= self.detector.get_cropped_face(faces)
        embs = []
        for face in faces:
            if len(face.shape) == 3:
                face = np.expand_dims(face, 0)
            face = face.astype(np.float32) / 255.
            embs.append(l2_norm(self.model(face)).numpy())

        list_min_idx = []
        list_score = []
        for emb in embs:
            dist = [euclidean(emb, self.embedding[i]) for i in self.embedding.keys()]
            min_idx = np.argmin(dist)
            list_min_idx.append(min_idx)
            list_score.append(dist[int(min_idx)])
        list_min_idx = np.array(list_min_idx)
       # print("minlist score",list_min_idx)
        list_score = np.array(list_score)
        #print("SSSCCCCOOOORRREEE",list_score)
        
        if list_score[0] < .93:
            list_min_idx[list_score > 1.5] = -1

            return self.name[list_min_idx[0]]
        else:
            return "Unknown"




#from preprocess import prepare_facebank, load_facebank, align_multi
# detector = DetectionMtcnn()
# path =os.getcwd()

# file = open(path+"/embds_dict_ad.pkl", 'rb')
# data = pickle.load(file)
# names = list(data.keys())
# class FACE_RECOGNITION:

# def main():
    

#     cfg = load_yaml(path+'/configs/arc_res50.yaml')

#     model = ArcFaceModel(size=cfg['input_size'],
#                          backbone_type=cfg['backbone_type'],
#                          training=False)

#     ckpt_path = tf.train.latest_checkpoint(path+'/checkpoints/' + cfg['sub_name'])
#     if ckpt_path is not None:
#         print("[*] load ckpt from {}".format(ckpt_path))
#         model.load_weights(ckpt_path)
#     else:
#         print("[*] Cannot find ckpt from {}.".format(ckpt_path))
#         exit()

#     cap = cv2.VideoCapture(0)

#     while cap.isOpened():
        
#         strat_time =datetime.datetime.now()
#         is_success, frame = cap.read()
#         if is_success:
#             img = frame
#         try:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             faces, bbox,landmarks= detector.get_cropped_face(frame)
#             # boxx = bbox[0]
#             bboxes = bbox
#             #bboxes=[float(i) for i in bboxes]
#             #print(bboxes)
#             embs = []
#             for face in faces:
#                 if len(face.shape) == 3:
#                     face = np.expand_dims(face, 0)
#                 face = face.astype(np.float32) / 255.
#                 embs.append(l2_norm(model(face)).numpy())

#             list_min_idx = []
#             list_score = []
#             for emb in embs:
#                 dist = [euclidean(emb, target) for target in data.values()]

#                 min_idx = np.argmin(dist)
#                 list_min_idx.append(min_idx)
#                 list_score.append(dist[int(min_idx)])
#             list_min_idx = np.array(list_min_idx)
#             #print(list_min_idx)
#             list_score = np.array(list_score)

#             if list_score.any()==False:
#                 continue
            
#             if list_score[0] < 1:
#                 list_min_idx[list_score > 1.2] = -1
#                 print("#############   Face matched   #############\n\n")
#                 print(bboxes)
#                 for idx, box in enumerate(bboxes):
#                     print("Name of the Detected Person:\n\n",  names[list_min_idx[idx]]) 
#                     print('\n\n')
#                     print("***********************************")
#                     frame = utils.draw_box_name(box,
#                                                 landmarks[idx],
#                                                 names[list_min_idx[idx]],
#                                                 frame)
#                 # cv2.imwrite("./known/"+str(strat_time)+".png", frame)
#                     # frame = cv2.rectangle(frame,(boxx[0],boxx[1]), (boxx[0]+boxx[2], boxx[1]+boxx[3]),(255, 250, 250),2)
#             else:
#                 print("###########     Warning      ##########")
#                 for idx, box in enumerate(bboxes):
#                     frame = utils.draw_box_name(box,
#                                                 landmarks[idx],
#                                                 "unknown",
#                                                 frame)
#                     # frame = cv2.rectangle(frame,(boxx[0],boxx[1]), (boxx[0]+boxx[2], boxx[1]+boxx[3]),(255, 250, 250),2)
            
                        
#         except:
#             continue
        
        
#         cv2.imshow('face Capture', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#             #cv2.imwrite('./save_frame/'+str(strat_time)+'.png',frame)
                 
#     cap.release()
#     cv2.destroyAllWindows()


# main()
