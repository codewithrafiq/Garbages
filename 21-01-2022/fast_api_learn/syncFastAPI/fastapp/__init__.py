from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



DATABASE_URL = "sqlite:///test.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapp import routes