from typing import List
from fastapi import APIRouter,status
from .models import Article,ArticleIn_Pydantic,Article_Pydantic, Status


route = APIRouter(tags=["Routes"])


@route.get("/")
async def Home():
    return {"message":"Welcome to the API"}


@route.get("/articles",response_model=List[Article_Pydantic])
async def Get_All_Articles():
    return await Article_Pydantic.from_queryset(Article.all())

@route.post("/article",response_model=Article_Pydantic)
async def Create_Article(article:ArticleIn_Pydantic):
    article_obj = await Article.create(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_tortoise_orm(article_obj)

@route.get("/article/{id}" ,response_model=Article_Pydantic)
async def Get_Article(id:int):
    article_obj = await Article.get(id=id)
    if not article_obj:
        return {"message":"Article not found"}    
    return await Article_Pydantic.from_tortoise_orm(article_obj)

@route.put("/article/{id}",response_model=Article_Pydantic)
async def Update_Article(id:int,article:ArticleIn_Pydantic):
    await Article.filter(id=id).update(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_tortoise_orm(await Article.get(id=id))


@route.delete("/article/{id}",response_model=Status)
async def Delete_Article(id:int):
    article_obj = await Article.get(id=id)
    await article_obj.delete()
    return {"message":f"Article {id} deleted"}




