
import os
import cv2
import glob
import time
import pickle
import numpy as np
from tqdm import tqdm
from PIL import Image
#from beckhend.src.align.test import DETECTION
import tensorflow as tf
from beckhend.src.modules import utils
# from beckhend.src.ALIGNMENT import ALIGN
from beckhend.src.modules.utils import l2_norm
from scipy.spatial.distance import euclidean
from beckhend.src.modules.models import ArcFaceModel
from beckhend.src.modules.evaluations import get_val_data, perform_val
from beckhend.src.modules.utils import set_memory_growth, load_yaml, l2_norm
#from beckhend.src.align_trans import warp_and_crop_face, get_reference_facial_points
from beckhend.mtcnn.MTCNN import DetectionMtcnn


class SAVE_EMBDED:
    def __init__(self):
        self.detector = DetectionMtcnn()
        self.embed = "./embds_dict_ad.pkl"
        self.input_size = 112
        self.backbone_type = 'ResNet50'
        self.sub_name = 'arc_res50'
        self.model = ArcFaceModel(size=self.input_size,
                         backbone_type=self.backbone_type,
                         training=False)
        self.ckpt_path = tf.train.latest_checkpoint('/home/sanaullah/Documents/Face-Recognition-v1/beckhend/checkpoints/' + self.sub_name)
       
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
        for image_name in glob.glob(path+"*"):
            print(image_name)
            if not image_name:
                continue
            else:
                name = image_name.split("/")[-1].split(".")[0]
                image = cv2.imread(image_name)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                print(image.shape)
                #image= cv2.copyMakeBorder(image,150,150,150,150,cv2.BORDER_CONSTANT,value=white)
                face, bbox= self.detector.get_cropped_face(image)
                print(len(face))
                face = face[0]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                #print(face[0])
                # img = np.array(face,dtype="uint8")
                cv2.imwrite("./crop/"+str(name)+".png",cv2.cvtColor(face, cv2.COLOR_BGR2RGB) )
                # print(face.shape)
                image = face.astype(np.float32) / 255.
                print(image.shape)
                #print(image.shape)
                # mirror = face.reshape(112,112,3)
                # mirror= cv2.flip(mirror, 1)
                # mirror= mirror.astype(np.float32) / 255.
                # mirror= mirror.reshape(1,112,112,3)
                # print(mirror.shape)
                if len(image.shape) == 3:
                    image = np.expand_dims(image, 0)
                    #mirror= np.expand_dims(mirror, 0)
            
                emb.append(l2_norm(self.model(image)).numpy()[0])
                names.append(name)
                
            
                
        # print("number of emb",len(emb))
        embd = np.asarray(emb)
        # print(" arry number of embd",embd.shape)

        nam = np.array(names)
        # print("*********** namea ************:",nam)
        embds_dict = dict(zip(nam, embd))
        # print(embds_dict)
        # print("*********** embds_dict ************:",embds_dict)
        print("*************    Prepareing embedding for save     **************")
        
        with open("./embds_dict_ad.pkl", "wb") as fi:
            bin_obj = pickle.dumps(embds_dict)
            fi.write(bin_obj)

        #return pickle.dump((embds_dict), open("./embds_dict_ad.pkl", 'ab'))
        print("*************     Embedding save Successfully    **************")

        return embds_dict
    
        #return pickle.dump(embds_dict, open("./embds_dict_ad.pkl", 'wb'))


    def update_face(self,image, name):

        emb=[]
        names=[]
        message ="Successfully Register"
        try:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)      
            # print(image.shape)
            #image= cv2.copyMakeBorder(image,150,150,150,150,cv2.BORDER_CONSTANT,value=white)
            face, bbox,_= self.detector.get_cropped_face(image)
            face = face[0].astype(np.float32) / 255.
            #print(image.shape)
            # mirror = face.reshape(112,112,3)
            # mirror= cv2.flip(mirror, 1)
            # mirror= mirror.astype(np.float32) / 255.
            # mirror= mirror.reshape(1,112,112,3)
            # print(mirror.shape)
            face =cv2.cvtColor(face, cv2.COLOR_BGR2RGB) 
            if len(face.shape) == 3:
                face = np.expand_dims(face, 0)
                #mirror= np.expand_dims(mirror, 0)
            
            emb.append(l2_norm(self.model(face)).numpy()[0])
            names.append(name)
            
            # print("number of emb",len(emb))
            embd = np.asarray(emb)
            # print(" arry number of embd",embd.shape)

            nam = np.array(names)
            # print("*********** namea ************:",nam)
            embds_dict = dict(zip(nam, embd))
            # print("*********** embds_dict ************:",embds_dict)
            #print("*************    Prepareing embedding for save     **************")
            
            with open("/home/sanaullah/Documents/face_rc_altersense/beckhend/embds_dict_ad.pkl", "rb") as fi:
                # bin_obj = pickle.dumps(embds_dict)
                file = pickle.load(fi)
            
            file.update(embds_dict)
            out_put = open("/home/sanaullah/Documents/face_rc_altersense/beckhend/embds_dict_ad.pkl", "wb")
            pickle.dump(file,out_put)
            out_put.close()
            
            # fi.write(bin_obj)

            #print("*************     Embedding save Successfully    **************")
            #return pickle.dump((embds_dict), open("./embds_dict_ad.pkl", 'ab'))
            return message

        except Exception as e:
            return e
