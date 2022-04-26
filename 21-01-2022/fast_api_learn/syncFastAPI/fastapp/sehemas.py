from pydantic import BaseModel

class ArticleSchema(BaseModel):
    title: str
    description: str

class MyArticleSchema(ArticleSchema):
    title: str
    description: str
    class Config:
        orm_mode = True


class TodoSchema(BaseModel):
    id: int
    title: str
    description: str
    class Config:
        orm_mode = True