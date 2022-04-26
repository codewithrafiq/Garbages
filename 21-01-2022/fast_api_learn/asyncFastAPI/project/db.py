import databases
from sqlalchemy import (
    MetaData,
    create_engine,
)
from databases import Database

DATABASE_URL = "sqlite:///project.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)