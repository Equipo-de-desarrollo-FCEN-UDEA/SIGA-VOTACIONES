from datetime import datetime
from typing import TYPE_CHECKING
from cuid import cuid

from sqlmodel import SQLModel, Field, Relationship

from app.models.enums import StatusName

if TYPE_CHECKING:
    from app.models.Voting import Voting

class StatusBase(SQLModel):
    name: StatusName

class Status(StatusBase, table=True):
    id: str | None = Field(primary_key=True)
    
    votings: list["Voting"] = Relationship(back_populates="status")   

    created_at: datetime | None = Field(default_factory=datetime.now, alias="createdAt")
    updated_at: datetime | None = Field(default_factory=datetime.now, alias="updatedAt")
    
    
class StatusCreate(StatusBase):
    pass

class StatusRead(StatusBase):
    id: str

class StatusReadWithVotings(StatusRead):
    from .Voting import VotingRead
    votings: list[VotingRead] = []

