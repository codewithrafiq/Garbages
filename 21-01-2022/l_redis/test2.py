import cv2
import redis
import random

redis_client = redis.Redis(host='localhost', port=6379)



def main():
    img = cv2.VideoCapture(0)
    while True:
        ret, frame = img.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        cv2.imwrite('test.jpg', frame)
        redis_client.set('test', )
        print('saved')
        cv2.waitKey(1)




if __name__ == '__main__':
    main()