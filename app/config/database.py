import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_app_settings
from app.core.settings.development import DevelopmentAppSettings

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

settings = DevelopmentAppSettings()
postgres_url = settings.database_uri

def get_engine(url: str = postgres_url):
    return create_engine(url, echo=True, pool_pre_ping=True)
                       
engine = get_engine(postgres_url)

def get_session():
    with Session(engine) as session:
        yield session

session = Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)