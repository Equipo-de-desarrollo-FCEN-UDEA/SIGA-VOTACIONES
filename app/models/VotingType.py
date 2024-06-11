from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from cuid import cuid

from app.models.Voting import Voting

class VotingTypeBase(SQLModel):
    concejo_id: str

class VotingType(VotingTypeBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votings: list[Voting] = Relationship(back_populates="voting_type")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class VotingTypeCreate(VotingTypeBase):
    pass

class VotingTypeUpdate(VotingTypeBase):
    pass

