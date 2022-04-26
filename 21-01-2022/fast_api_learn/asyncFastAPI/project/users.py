from typing import List
from project import articles
from fastapi import HTTPException
from . schema import UserSchema,UserSchema2
from . models import User
from project import database
from fastapi import APIRouter
from passlib.hash import pbkdf2_sha256

router = APIRouter(tags=["Users"])


@router.get("/users", response_model=List[UserSchema2])
async def get_all_users():
    query = User.select()
    return await database.fetch_all(query)

@router.post("/users", response_model=UserSchema2)
async def create_user(user: UserSchema):
    hash_password = pbkdf2_sha256.hash(user.password)
    query = User.insert().values(username=user.username, password=hash_password)
    last_record_id = await database.execute(query)
    return {**user.dict(),"id": last_record_id}


@router.get("/users/{user_id}", response_model=UserSchema2)
async def get_user(user_id: int):
    query = User.select().where(user_id == User.c.id)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

