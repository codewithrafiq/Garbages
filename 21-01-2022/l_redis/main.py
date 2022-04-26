from fastapi import FastAPI
import uvicorn
import redis
import cv2
import random
import numpy as np


redis_client = redis.Redis(host='localhost', port=6379)
app = FastAPI()



redis_client.mset({'key1': 'value1', 'key2': 'value2'})
redis_client.psetex('key3', 9000, 'value3')




# def get_frames():


    # img = cv2.VideoCapture(0)
    # while True:
    #     ret, frame = img.read()
    #     img_str = cv2.imencode('.jpg', frame)[1].tostring()
        


        # key = random.randint(0, 1000000)
        # redis_client.set(key, frame)


        # redis_client.set(key, frame.tobytes())
        # img_str = redis_client.get(key)


        # img_np = cv2.imread(img_str,mode='RGB')

        # cv2.imshow('frame', img_np)
        # cv2.waitKey(1)




if __name__ == '__main__':
    # get_frames()
    pass