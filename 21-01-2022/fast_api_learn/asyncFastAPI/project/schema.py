from pydantic import BaseModel
from typing import Optional


class ArticleSchema(BaseModel):
    title: str
    description: str
    

class ArticleSchema2(BaseModel):
    id: int
    title: str
    description: str
    

class TodoSchema(BaseModel):
    id: int
    title: str
    description: str

class UserSchema(BaseModel):
    username: str
    password: str

class UserSchema2(BaseModel):
    id: int
    username: str

class LoginSchema(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    username: Optional[str] = None