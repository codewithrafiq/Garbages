from fastapi import FastAPI
from project.utils import call_me
from pathlib import Path


demo = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent

call_me()