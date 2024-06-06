from app.services.base import ServiceBase
from app.schemas.user import UserUpdate, UserCreate
from app.protocols.db.models.user import User
from app.protocols.db.crud.user import CRUDUserProtocol


class UserService(ServiceBase[User, UserCreate, UserUpdate, CRUDUserProtocol]):
    ...


user_svc = UserService()