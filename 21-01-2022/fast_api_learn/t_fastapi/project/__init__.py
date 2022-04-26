from fastapi import FastAPI



app = FastAPI()





import project.route
from project.route2 import route2

# app.include_router(route1)
app.include_router(route2)