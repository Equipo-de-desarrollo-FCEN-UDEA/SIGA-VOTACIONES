from datetime import datetime
from typing import List

from cuid import cuid

from sqlmodel import SQLModel, Field, Relationship

from app.models.enums import StatusName
from app.models.Vote import Vote
from app.models.VotingType import VotingType


class VotingBase(SQLModel):
    maxVotes: int
    status: StatusName | None = Field(default=None, foreing_key="status.id")
    type_id: VotingType | None = Field(default=None, foreing_key="type.id")

class Voting(VotingBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votes: List[Vote] = Relationship(back_populates="voting")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")
    
class VotingCreate(VotingBase):
    pass

class VotingRead(VotingBase):
    id: str