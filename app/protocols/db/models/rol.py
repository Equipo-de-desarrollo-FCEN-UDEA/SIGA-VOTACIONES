from app.protocols.db.utils.model import BaseModel

class Rol(BaseModel):
    name: str
    description:str | None