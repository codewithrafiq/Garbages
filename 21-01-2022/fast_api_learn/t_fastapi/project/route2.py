from fastapi import APIRouter


route2 = APIRouter(tags=["Route2"])


@route2.get("/2")
def route1_get():
    return {"message": "Hello from route1"}