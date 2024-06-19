from datetime import datetime
from typing import TYPE_CHECKING
from cuid import cuid

from sqlmodel import SQLModel, Field, Relationship

from app.models.Status import Status, StatusRead

if TYPE_CHECKING:
    from app.models.Vote import Vote

from app.models.MeetType import MeetType


class VotingBase(SQLModel):
    maxVotes: int
    status_id: str | None = Field(default=None, foreign_key="status.id")
    meet_type_id: str | None = Field(default=None, foreign_key="meettype.id")

class Voting(VotingBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votes: list["Vote"] = Relationship(back_populates="voting")
    
    status: Status = Relationship(back_populates="votings")
    meet_type: MeetType = Relationship(back_populates="votings")
    
    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")
    
class VotingCreate(VotingBase):
    pass

class VotingRead(VotingBase):
    id: str

class VotingReadWithInfo(VotingRead):
    from app.models.Vote import VoteRead
    status: StatusRead | None = None
    votes: list[VoteRead] = []
