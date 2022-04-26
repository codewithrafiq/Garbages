from turtle import clear
from celery import Celery
from time import sleep

# app = Celery(broker='redis://localhost:6379/0')
app = Celery(broker="192.168.1.233:1883")


"""
***** Command Line Codes *****

> celery -A server worker --loglevel=info

>>> from server import add
>>> add.delay(4,4)


"""
@app.task
def add(x, y):
    sleep(5)
    return x + y

