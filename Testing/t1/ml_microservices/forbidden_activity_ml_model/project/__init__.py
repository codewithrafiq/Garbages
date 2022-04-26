from fastapi import FastAPI
from pathlib import Path
from project.utils import videoFeed

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

# print("apppp------>")


videoFeed()
