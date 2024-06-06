from app.protocols.db.utils.model import BaseModel


class User(BaseModel):
    uid: str
    email: str
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None

    # pets: list[Any]