from os import access
from typing import List
from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi.param_functions import Depends
from starlette.responses import HTMLResponse
from .schema import LoginSchema
from .models import Article, User
from .db import database
from passlib.hash import pbkdf2_sha256
from . Token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Auth"])


@router.post("/login/")
async def login(request:OAuth2PasswordRequestForm=Depends()):
    query = User.select().where(User.c.username == request.username)
    myuser = await database.fetch_one(query)
    if not myuser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username")
    if not pbkdf2_sha256.verify(request.password, myuser.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    access_token = create_access_token(
        data={"sub": myuser.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

