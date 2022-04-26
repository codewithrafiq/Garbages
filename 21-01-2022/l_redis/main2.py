import cv2
import numpy as np
import redis
import random



redis_client = redis.Redis(host='localhost', port=6379)



def get_frames():
    """
    Image to Text and Text to Image
    """
    img = cv2.VideoCapture(0)
    while True:
        ret, frame = img.read()
        img_str1 = cv2.imencode('.jpg', frame)[1].tostring()

        key = random.randint(0, 1000000)
        redis_client.set(key, img_str1,ex=5)

        img_str2 = redis_client.get(key)
        img_np = cv2.imdecode(np.frombuffer(img_str2, np.uint8), 1)
        
        cv2.imshow('frame', img_np)
        cv2.waitKey(1)

get_frames()