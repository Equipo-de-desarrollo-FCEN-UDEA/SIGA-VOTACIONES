from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUserProtocol(CRUDProtocol[User, UserCreate, UserUpdate]):
    ...