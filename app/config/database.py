import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_app_settings

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
posgres_url = "postgresql://postgres:postgres@vote-db:5432/vote_db"

settings = get_app_settings()

#connect_args = {"check_same_thread": False}
engine = create_engine(posgres_url, echo=True, 
                       pool_pre_ping=True)

Session = Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)