from re import L
import cv2
from project.ml.face_recog.project.libs.recognition.RECOGNITION import RECOG
from project.ml.prj.detector.detector import ABSENSE
from project.ml.people.demo import PEOPLE
import numpy as np
import datetime
import pickle

class WORKER_COUNTER:
    
    def __init__(self):
        self.embed = "./face_recog/project/information/embdding.pkl"
        self.centerface = PEOPLE()
        self.recog = RECOG()

    def load_pickle(self,path):
        file = open(path,'rb')
        embedding = pickle.load(file)
        name =[]
        for i in embedding.keys():
            name.append(i)
        return name, embedding

    def camera(self, frame):
        # print("ABSENCE",frame.shape)
       
        
       
        names, embedding = self.load_pickle(self.embed)
        # print(names)
        missing_list =[]
        tota_time_more ={}
        # print("ABSENt",frame.shape)
        number = self.centerface.count_number(frame)
        # print('------------------------', number)
        try:
            start = datetime.datetime.now()
            if number > 5:
                start_time = datetime.datetime.now()
                # print("Kichu Romantic JIN or PORI Dating marte ---------[ASHCHE] ")
                name, face = self.recog.recognition(frame)
                # print('Dating marte ashche',name, face )
                if name =="Unknown":
                    end_time = datetime.datetime.now()
                    diff = end_time-start_time
                    if name not in tota_time_more.keys():
                        tota_time_more[name] = diff
                    else:
                        tota_time_more[name] = tota_time_more.get(name) + diff
                    return {"image":face,"time":diff} 
                else:
                    return None 
            if (number < 5) :
                loss_time_start = datetime.datetime.now()
                # print("Kichu Romantic JIN or PORI Dating marte ---------[@@@@@@@@] ")
                name, face = self.recog.recognition(frame)
                missing_list.append(name)
                loss_time_end = datetime.datetime.now()
                name_list  = sorted(set(missing_list))
                a =(set(name_list).difference(names))
                if len(a)==0:
                    return "OK", "OK"
                else:
                    a =np.array(list(a)[0])
                    # print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",a)
                    diff = loss_time_end-loss_time_start
                    if a not in tota_time_more.keys():
                        tota_time_more[a] = diff
                    else:
                        tota_time_more[a] = tota_time_more.get(a) + diff
                    
                    return a,diff,loss_time_start,loss_time_end

        except Exception as e: 
            print(e)


