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
        print(self.path)
        self.detector = DetectionMtcnn()
        self.embed = "./beckhend/embds_dict_ad.pkl"
        self.input_size = 112
        self.backbone_type = 'ResNet50'
        self.sub_name = 'arc_res50'
        self.model = ArcFaceModel(size=self.input_size,
                         backbone_type=self.backbone_type,
                         training=False)
        self.ckpt_path = tf.train.latest_checkpoint('./beckhend/checkpoints/' + self.sub_name)

        if self.ckpt_path is not None:
            print("[*] load ckpt from {}".format(self.ckpt_path))
            self.model.load_weights(self.ckpt_path)
        else:
            print("[*] Cannot find ckpt from {}.".format(self.ckpt_path))
            exit()
        
        self.names, self.embedding = load_pickle(self.embed)


    def recognition(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        faces, bbox,landmarks= self.detector.get_cropped_face(frame)
        
        bboxes = bbox
        embs = []
        for face in faces:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
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
        list_score = np.array(list_score)
        if list_score.any()==False:
            pass
        if list_score[0] < 1:
            list_min_idx[list_score > 1.2] = -1
            for idx, box in enumerate(bboxes):
                print(self.names[list_min_idx[idx]])
                frame = utils.draw_box_name(box,
                                            landmarks[idx],
                                            self.names[list_min_idx[idx]],
                                            frame)
            
        else:

            for idx, box in enumerate(bboxes):
                frame = utils.draw_box_name(box,
                                            landmarks[idx],
                                            "unknown",
                                            frame)
        
        return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 

        

        


