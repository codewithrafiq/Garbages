
import os
import cv2
import glob
import time
import pickle
import numpy as np
from tqdm import tqdm
from PIL import Image
import tensorflow as tf
from mlutils.libs.recognition.modules import utils
from mlutils.libs.recognition.modules.utils import l2_norm
from scipy.spatial.distance import euclidean
from mlutils.libs.recognition.modules.models import ArcFaceModel
from mlutils.libs.recognition.modules.evaluations import get_val_data, perform_val
from mlutils.libs.recognition.modules.utils  import set_memory_growth, load_yaml, l2_norm
from mlutils.libs.detector.MTCNN import DetectionMtcnn


class SAVE_EMBDED:
    def __init__(self):
        self.detector = DetectionMtcnn()
        # self.embed = np.load("./embedding.npy", allow_pickle = True)
        # self.name = np.load("./name.npy", allow_pickle = True)
        self.input_size = 112
        self.backbone_type = 'ResNet50'
        self.sub_name = 'arc_res50'
        self.model = ArcFaceModel(size=self.input_size,
                         backbone_type=self.backbone_type,
                         training=False)
        self.ckpt_path = tf.train.latest_checkpoint('mlutils/checkpoints/' + self.sub_name)
       
        if self.ckpt_path is not None:
            print("[*] load ckpt from {}".format(self.ckpt_path))
            self.model.load_weights(self.ckpt_path)
        else:
            print("[*] Cannot find ckpt from {}.".format(self.ckpt_path))
            exit()

    def save_multiple_embed(self,path):
     
        names = []
        emb=[]
        embeddings=[]
        name =[]
        for image_name in glob.glob(path+"*"):
            print(image_name)
            if not image_name:
                continue
            else: 
                name = image_name.split("/")[-1].split(".")[0]
                image = cv2.imread(image_name)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                face, bbox,_= self.detector.get_cropped_face(image)
                image = face[0]   
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = image.astype(np.float32) / 255.
                #mirror = image.reshape(112,112,3)
                mirror= cv2.flip(image, 1)
                mirror= mirror.astype(np.float32) / 255.
                if len(image.shape) == 3:
                    image = np.expand_dims(image, 0)
                    mirror= np.expand_dims(mirror, 0)
                image = l2_norm(self.model(image))
                mirror = l2_norm(self.model(mirror))
                ebd = np.mean([image, mirror],axis=0)
                emb.append(ebd)
                names.append(name)
        embd = np.asarray(emb)
        nam = np.array(names)
        embds_dict = dict(zip(nam, embd))
        with open("mlutils/information/embdding.pkl", "wb") as fi:
            bin_obj = pickle.dumps(embds_dict)
            fi.write(bin_obj)
        return "sucessfull", "200"




    def register(self,image, name):
        emb=[]
        names=[]
        

        # try:

        #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)      
        #     print(image.shape)
        #     face, bbox,_= self.detector.get_cropped_face(image)
        #     face =face[0]
        #     face =cv2.cvtColor(face, cv2.COLOR_BGR2RGB) 
        #     face = face.astype(np.float32) / 255.
        #     print(image.shape)
        #     mirror = face.reshape(112,112,3)
        #     mirror= cv2.flip(mirror, 1)
        #     mirror= mirror.astype(np.float32) / 255.
        #     if len(face.shape) == 3:
        #         face = np.expand_dims(face, 0)
        #         mirror= np.expand_dims(mirror, 0)
        #     image = l2_norm(self.model(face))
        #     mirror = l2_norm(self.model(mirror))
        #     ebd = np.mean([image, mirror],axis=0)
        #     emb.append(ebd)
        #     names.append(name)
        #     embd = np.asarray(emb)
        #     nam = np.array(names)
        #     embds_dict = dict(zip(nam, embd))
        #     with open("project/utils/information/embdding.pkl", "wb") as fi:
        #         bin_obj = pickle.dumps(embds_dict)
        #         fi.write(bin_obj)
            
        #     return "sucesssfull", "200"
        # except:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)      
        print(image.shape)
        face, bbox,_= self.detector.get_cropped_face(image)
        if len(bbox) == 1:
            face =face[0]
            face =cv2.cvtColor(face, cv2.COLOR_BGR2RGB) 
            face = face.astype(np.float32) / 255.
            print(image.shape)
            mirror = face.reshape(112,112,3)
            mirror= cv2.flip(mirror, 1)
            mirror= mirror.astype(np.float32) / 255.
            if len(face.shape) == 3:
                face = np.expand_dims(face, 0)
                mirror= np.expand_dims(mirror, 0)
            image = l2_norm(self.model(face))
            mirror = l2_norm(self.model(mirror))
            ebd = np.mean([image, mirror],axis=0)
            emb.append(ebd)
            names.append(name)
            embd = np.asarray(emb)
            nam = np.array(names)
            embds_dict = dict(zip(nam, embd))
            with open("mlutils/information/embdding.pkl", "rb") as fi:
                file = pickle.load(fi)
            file.update(embds_dict)
            out_put = open("mlutils/information/embdding.pkl", "wb")
            pickle.dump(file,out_put)
            out_put.close()
            return 200
        else:
            return  500
