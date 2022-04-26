from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
)
from .db import metadata





Article = Table(
    "article",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(300)),
)

Todo = Table(
    "todo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(300)),
)

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100)),
    Column("password", String(500)),
)
