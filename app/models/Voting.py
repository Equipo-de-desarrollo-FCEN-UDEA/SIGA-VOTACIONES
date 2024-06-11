from datetime import datetime
from typing import List

from cuid import cuid

from sqlmodel import SQLModel, Field, Relationship

from app.schemas.enums import StatusName
from app.schemas.vote import Vote



class VotingBase(SQLModel):
    status: StatusName
    

class Voting(VotingBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votes: List[Vote] = Relationship(back_populates="voting")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")