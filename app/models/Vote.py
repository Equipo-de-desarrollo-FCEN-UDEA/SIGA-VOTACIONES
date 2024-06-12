# vote.py
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from app.models import Voting
from app.models.enums import VoteType

class VoteBase(SQLModel):
    vote_type: VoteType

    user_id: str = Field(primary_key=True)
    voting_id: str = Field(foreign_key="voting.id", primary_key=True)
    

class Vote(VoteBase):
    voting: Voting = Relationship(back_populates="votes")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class VoteCreate(VoteBase):
    pass

class VoteRead(VoteBase):
    pass

class VoteUpdate(SQLModel):
    vote_type: VoteType
