from sqlmodel import SQLModel, Field
from cuid import cuid


class Prueba2Base(SQLModel):
    vote_type: str
    user_id: int
    voting_id: str | None = Field(default=None, foreign_key="voting.id")


class Prueba2(Prueba2Base, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)
    
    

class Prueba2Create(Prueba2Base):
    pass