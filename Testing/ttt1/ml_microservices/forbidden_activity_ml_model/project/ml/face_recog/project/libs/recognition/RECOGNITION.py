import os
import cv2
from time import time
# from beckhend.main import utils
import pickle
import datetime
import numpy as np
import tensorflow as tf
from project.ml.face_recog.project.libs.detector.MTCNN import DetectionMtcnn
from project.ml.face_recog.project.libs.recognition.modules.models import ArcFaceModel
from scipy.spatial.distance import euclidean
from project.ml.face_recog.project.libs.recognition.modules.utils import set_memory_growth, load_yaml, l2_norm


def load_pickle(path):
    file = open(path,'rb')
    embedding = pickle.load(file)
    name =[]
    for i in embedding.keys():
        name.append(i)
    return name, embedding


class RECOG:
    
    def __init__(self):
        self.detector = DetectionMtcnn()
        self.embed = "project/ml/face_recog/project/information/embdding.pkl"
        self.input_size = 112
        self.backbone_type = 'ResNet50'
        self.sub_name = 'arc_res50'
        self.model = ArcFaceModel(size=self.input_size,
                         backbone_type=self.backbone_type,
                         training=False)
        self.ckpt_path = tf.train.latest_checkpoint('project/ml/face_recog/project/checkpoints/' + self.sub_name)

        if self.ckpt_path is not None:
            print("[*] load ckpt from {}".format(self.ckpt_path))
            self.model.load_weights(self.ckpt_path)
        else:
            print("[*] Cannot find ckpt from {}.".format(self.ckpt_path))
            exit()
        
        self.names, self.embedding = load_pickle(self.embed)


    def recognition(self,frame):
        # print("recognition----------------->",frame.shape)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        faces, bbox ,landmarks= self.detector.get_cropped_face(frame)
        
        # print("faces---->",faces[0].shape)
        # cv2.imwrite("image.png", faces[0])
        # # images = faces[0]
        bboxes = bbox
        embs = []
        for face in faces:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            # print("_____________________>>>",face.shape)
            mirror= cv2.flip(face, 1)
            if len(face.shape) == 3:
                face = np.expand_dims(face, 0)
                mirror = np.expand_dims(mirror, 0)
            face = face.astype(np.float32) / 255.
            # print("_____________________>>>",face.shape)
            mirror = mirror.astype(np.float32) / 255.
            # print("---------------------------------->>>",mirror.shape)
            face =(l2_norm(self.model(face)))
            mirror =(l2_norm(self.model(mirror)))
            embd = np.mean([face, mirror],axis=0)
            # print("mirror------------------>>>",mirror)
            # print("Embedding------------------>>>",embd)
            embs.append(embd)
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
                print("")
            
            return self.names[list_min_idx[idx]]
        else:

            for idx, box in enumerate(bboxes):
                print("")     
            return "Unknown"




    def recognize_worker(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        faces, bbox ,landmarks= self.detector.get_cropped_face(frame)
        
        # print("faces",faces[0].shape)
        # cv2.imwrite("image.png", faces[0])
        # images = faces[0]
        bboxes = bbox
        embs = []
        now = time.time()
        for face in faces:
            # cv2.imwrite(str(now)+".png",face)
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            # print("_____________________>>>",face.shape)
            mirror= cv2.flip(face, 1)
            if len(face.shape) == 3:
                face = np.expand_dims(face, 0)
                mirror = np.expand_dims(mirror, 0)
            face = face.astype(np.float32) / 255.
            # print("_____________________>>>",face.shape)
            mirror = mirror.astype(np.float32) / 255.
            # print("---------------------------------->>>",mirror.shape)
            face =(l2_norm(self.model(face)))
            mirror =(l2_norm(self.model(mirror)))
            embd = np.mean([face, mirror],axis=0)
            # print("mirror------------------>>>",mirror)
            # print("Embedding------------------>>>",embd)
            embs.append(embd)
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
                print("")
            
            return self.names[list_min_idx[idx]]
        else:

            for idx, box in enumerate(bboxes):
                print("")     
            return "Unknown"

        



    def lenght_bbox(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        faces, bbox ,landmarks= self.detector.get_cropped_face(frame)
        
        return len(bbox)

      
    # def service_que(self,frame):
        
    #     embs = []
    #     face = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     # print("_____________________>>>",face.shape)
    #     mirror= cv2.flip(face, 1)
    #     if len(face.shape) == 3:
    #         face = np.expand_dims(face, 0)
    #         mirror = np.expand_dims(mirror, 0)
    #     face = face.astype(np.float32) / 255.
    #     # print("_____________________>>>",face.shape)
    #     mirror = mirror.astype(np.float32) / 255.
    #     # print("---------------------------------->>>",mirror.shape)
    #     face =(l2_norm(self.model(face)))
    #     mirror =(l2_norm(self.model(mirror)))
    #     embd = np.mean([face, mirror],axis=0)
    #     # print("mirror------------------>>>",mirror)
    #     # print("Embedding------------------>>>",embd)
    #     embs.append(embd)
    #     list_min_idx = []
    #     list_score = []
    #     for emb in embs:
    #         dist = [euclidean(emb, self.embedding[i]) for i in self.embedding.keys()]
    #         min_idx = np.argmin(dist)
    #         list_min_idx.append(min_idx)
    #         list_score.append(dist[int(min_idx)])
    #     list_min_idx = np.array(list_min_idx)
    #     list_score = np.array(list_score)
    #     if list_score.any()==False:
    #         pass
    #     if list_score[0] < 1:
    #         list_min_idx[list_score > 1.2] = -1
    #         for idx, box in enumerate(bboxes):
    #             print("")
    #         return self.names[list_min_idx[idx]]
    #     else:

    #         for idx, box in enumerate(bboxes):
    #             print("")     
    #         return "Unknown"


