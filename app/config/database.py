import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_app_settings

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

settings = get_app_settings()

def get_engine(url: str = database_url):
    return create_engine(url, echo=True)

engine = get_engine(database_url)

def get_session():
    with Session(engine) as session:
        yield session

session = Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)