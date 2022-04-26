from fastapp import Base
from sqlalchemy import Column, Integer, String


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(300))

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(300))
