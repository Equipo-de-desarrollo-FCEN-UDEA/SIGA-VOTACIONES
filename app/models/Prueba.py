from sqlmodel import Relationship, SQLModel, Field
from app.models.Voting import Voting
from datetime import datetime
from cuid import cuid


class PruebaBase(SQLModel):
    name: str 

    voting_id: str = Field(foreign_key="voting.id", primary_key=True)

class Prueba(PruebaBase, table=True):
    usuario: str = Field(primary_key=True)
    
    voting: Voting = Relationship(back_populates="pruebas")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class PruebaCreate(PruebaBase):
    usuario: str

class PruebaRead(PruebaBase):
    usuario: str