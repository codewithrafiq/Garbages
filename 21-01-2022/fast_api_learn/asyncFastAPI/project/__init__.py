from fastapi import FastAPI
from starlette.responses import HTMLResponse
from .db import database
from fastapi import APIRouter

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


from project import models
from project import articles
from project import users
from project import auth


app.include_router(articles.router)
app.include_router(users.router)
app.include_router(auth.router)



@app.get('/', response_class=HTMLResponse)
def index():
    return """
    <h1><a href="/docs">Docs</a></h1>
    <h1><a href="/redoc">Redoc</a></h1>
    """
