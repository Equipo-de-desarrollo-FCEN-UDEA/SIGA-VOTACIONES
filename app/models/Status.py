from datetime import datetime
from typing import List
from typing import TYPE_CHECKING
from cuid import cuid

from sqlmodel import SQLModel, Field, Relationship

from app.models.enums import StatusName

if TYPE_CHECKING:
    from app.models.Voting import Voting

class StatusBase(SQLModel):
    name: StatusName

class Status(StatusBase, table=True):
    id: str | None = Field(default=cuid(), primary_key=True)
    
    votings: List["Voting"] = Relationship(back_populates="status")   

    created_at: datetime | None = Field(default_factory=datetime.now, alias="createAt")
    updated_at: datetime | None = Field(default_factory=datetime.now, alias="updateAt")
    
    
class StatusCreate(StatusBase):
    pass

class StatusRead(StatusBase):
    id: str

