from sqlmodel import Session, SQLModel
from typing import Type

class BasePolicy:
    def __init__(self, db: Session, model: Type[SQLModel]):
        self.db = db
        self.model = model