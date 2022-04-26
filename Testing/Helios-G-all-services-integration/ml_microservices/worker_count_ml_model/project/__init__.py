from fastapi import FastAPI
from project.utils import VideoFeed

app = FastAPI()

vf = VideoFeed()
vf.start()
