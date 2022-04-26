import cv2
from mlutils.libs.detector.MTCNN import DetectionMtcnn
from mlutils.libs.recognition.RECOGNITION import RECOG
from mlutils.libs.register.REGISTER import SAVE_EMBDED


class ALL_FUNCTIONS:
    def __init__(self):

        self.detector = DetectionMtcnn()
        self.recog = RECOG()
        self.trains = SAVE_EMBDED()


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

        if image is not None:
            try:
                result = self.recog.recognition(image)
                if result =="unknown":
                    return {"result": result, "status":202}
                else:
                    return {"result": result, "status":200}

            except Exception as e:
                return {"error":str(e),"status":500}
        else:
            return {"message":"No image found","status":202}




    def registration(self,image,ID):

        if image is not None:
            try:
                result = self.trains.register(image, ID)
                return result

            except Exception as e:
                return 500

        else:
            return 500




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
