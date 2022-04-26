from fastapi import APIRouter
from project import app



route1 = APIRouter(tags=["Route1"])


@app.get("/")
def route1_get():
    return {"message": "Hello from route1"}
@app.get("/")
def route1_get():
    return {"message": "Hello from route1"}
@app.get("/")
def route1_get():
    return {"message": "Hello from route1"}
@app.get("/")
def route1_get():
    return {"message": "Hello from route1"}