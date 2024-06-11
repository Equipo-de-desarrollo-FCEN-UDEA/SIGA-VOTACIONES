# vote.py
from typing import Optional
from cuid import cuid
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from app.schemas.enums import VoteType

class VoteBase(SQLModel):
    vote_type: VoteType
    user_id: int
    voting_id: str = Field(foreign_key="voting.id")

class Vote(VoteBase):
    id: str = Field(default=cuid(), primary_key=True)

    voting: "voting" = Relationship(back_populates="votes") # type: ignore

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class VoteCreate(VoteBase):
    pass

class VoteUpdate(VoteBase):
    pass
