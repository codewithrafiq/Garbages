from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class Article(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()

    class PydanticMeta:
        pass

Article_Pydantic = pydantic_model_creator(Article, name='Article')
ArticleIn_Pydantic = pydantic_model_creator(Article, name='ArticleIn',exclude_readonly=True)



class Status(BaseModel):
    message: str















