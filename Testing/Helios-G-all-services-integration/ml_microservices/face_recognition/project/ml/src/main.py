import cv2
from project.ml.libs.detector.MTCNN import DetectionMtcnn
from project.ml.libs.recognition.RECOGNITION import RECOG
from project.ml.libs.register.REGISTER import SAVE_EMBDED

class ALL_FUNCTIONS:
    def __init__(self):

        self.detector = DetectionMtcnn()
        self.recog = RECOG()
        self.train = SAVE_EMBDED()


    def detection(self, image):
      
        if image is not None:
            try:
                face,bbox,face_points = self.detector.get_cropped_face(image)

                return {"face":face, "bbox":bbox, "face_points":face_points}
            except Exception as e:
                return {"error":str(e)}
        else:
            return {"message":"No image found"}



    def recognition(self, image):

        # cv2.imwrite("test.png",image)
        if image is not None:
            try:
                result = self.recog.recognition(image)
                print("result------>",result)
                if result =="Unknown":
                    return "unknown"
                else:
                    return result

            except Exception as e:
                return 'unknown'
        else:
            return "unknown"




    def registration(self,image,ID):

        if image is not None:
            try:
                result = self.train.register(image, ID)
                return {"result": result,"message":"200"}

            except Exception as e:
                return {"error":str(e)}

        else:
            return {"message":"No image found"}




    def train(self,path):

        if path is not None:
            try:
                result = self.train.save_multiple_embed(path)
                return {"result": result,"message":"200"}

            except Exception as e:
                return {"error":str(e)}
        else:
            return {"message":"Path Invalid No image found"}





    def queueing(self, image):

        if image is not None:
            try:
                result = self.recog.service_que(image)
                return {"result": result,"message":"200"}
                
            except Exception as e:
                return {"error":str(e)}
        else:
            return {"message":" Invalid No image found"}
    
    def number_people(self,image):

        number = self.recog.lenght_bbox(image)

        return number
    
    def worker_recognition(self, image):

        name = self.recog.recognize_worker(image)

        return name


