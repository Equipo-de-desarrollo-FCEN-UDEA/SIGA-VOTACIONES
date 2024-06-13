from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from cuid import cuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.Voting import Voting

class VotingTypeBase(SQLModel):
    concejo_id: str

class VotingType(VotingTypeBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votings: list["Voting"] = Relationship(back_populates="type")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class VotingTypeCreate(VotingTypeBase):
    pass

class VotingTypeRead(VotingTypeBase):
    pass

class VotingTypeUpdate(VotingTypeBase):
    pass

