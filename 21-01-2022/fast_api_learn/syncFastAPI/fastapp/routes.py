from fastapp import app,get_db
from .models import Article
from .sehemas import ArticleSchema,MyArticleSchema
from fastapi import Depends,status
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/articles/",response_model=List[MyArticleSchema])
def getArticles(db: Session = Depends(get_db)):
    myarticles = db.query(Article).all()
    return myarticles

@app.get("/articles/{id}",response_model=MyArticleSchema,status_code=status.HTTP_200_OK)
def getArticle(id: int,db: Session = Depends(get_db)):
    # article = db.query(Article).filter(Article.id == id).first()
    article = db.query(Article).get(id)
    if article:
        return article
    raise HTTPException(status_code=404, detail="Article not found")

@app.post("/articles/",status_code=status.HTTP_201_CREATED)
def create_article(article: ArticleSchema,db:Session=Depends(get_db)):
    new_article = Article(title=article.title,description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


@app.put("/articles/{id}",status_code=status.HTTP_200_OK)
def update_article(id: int,article: ArticleSchema,db:Session=Depends(get_db)):
    print(article)
    article_to_update = db.query(Article).get(id)
    if article_to_update:
        article_to_update.title = article.title
        article_to_update.description = article.description
        db.commit()
        db.refresh(article_to_update)
        return article_to_update
    raise HTTPException(status_code=404, detail="Article not found")

@app.delete("/articles/{id}",status_code=status.HTTP_200_OK)
def delete_article(id: int,db:Session=Depends(get_db)):
    article_to_delete = db.query(Article).get(id)
    if article_to_delete:
        db.delete(article_to_delete)
        db.commit()
        return {"message":"Article deleted"}
    raise HTTPException(status_code=404, detail="Article not found")