from typing import List
from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi.param_functions import Depends
from starlette.responses import HTMLResponse
from .schema import ArticleSchema, ArticleSchema2, UserSchema, UserSchema2
from .models import Article
from .db import database
from .Token import get_current_user

router = APIRouter(tags=["Articles"])


@router.post('/article/', status_code=status.HTTP_201_CREATED, response_model=ArticleSchema2)
async def add_article(article: ArticleSchema,current_user:UserSchema = Depends(get_current_user)):
    query = Article.insert().values(title=article.title,
                                    description=article.description)
    last_record_id = await database.execute(query)
    return {**article.dict(), 'id': last_record_id}


@router.get('/articles/', status_code=status.HTTP_200_OK, response_model=List[ArticleSchema])
async def get_articles(current_user:UserSchema = Depends(get_current_user)):
    query = Article.select()
    return await database.fetch_all(query)


@router.get('/article/{id}', status_code=status.HTTP_200_OK, response_model=ArticleSchema)
async def get_article(id: int,current_user:UserSchema = Depends(get_current_user)):
    query = Article.select().where(id == Article.c.id)
    data = await database.fetch_one(query)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')
    return {**data}


@router.put('/article/{id}', status_code=status.HTTP_200_OK, response_model=ArticleSchema)
async def update_article(id: int, article: ArticleSchema,current_user:UserSchema = Depends(get_current_user)):
    query = Article.update().where(id == Article.c.id).values(
        title=article.title, description=article.description)
    await database.execute(query)
    if not await database.execute(query):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')
    return {**article.dict(), "id": id}


@router.delete('/article/{id}', status_code=status.HTTP_200_OK)
async def delete_article(id: int,current_user:UserSchema = Depends(get_current_user)):
    query = Article.delete().where(id == Article.c.id)
    if await database.execute(query) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')
    await database.execute(query)
    return {'id': id, 'message': 'Article deleted'}
