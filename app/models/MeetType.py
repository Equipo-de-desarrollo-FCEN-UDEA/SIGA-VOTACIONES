from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from cuid import cuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.Voting import Voting

class MeetTypeBase(SQLModel):
    department_id: str
    rol_id: str

class MeetType(MeetTypeBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)

    votings: list["Voting"] = Relationship(back_populates="meet_type")

    created_at: datetime = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.now, alias="updateAt")

class MeetTypeCreate(MeetTypeBase):
    pass

class MeetTypeRead(MeetTypeBase):
    id: str

class MeetTypeUpdate(MeetTypeBase):
    pass

