from typing import Optional
from cuid import cuid
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from app.models.enums import VoteType
from app.models.Voting import Voting


class VoteBase(SQLModel):
    vote_type: VoteType
    user_id: int
    voting_id: str = Field(foreign_key="votings.id")

class Vote(VoteBase):
    id: str = Field(default=cuid(), primary_key=True)

    voting: Voting = Relationship(back_populates="votes")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class VoteCreate(VoteBase):
    pass

class VoteUpdate(VoteBase):
    pass
