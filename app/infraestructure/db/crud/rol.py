from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Rol
from app.schemas.rol import RolCreate, RolUpdate


class UserCrud(CRUDBase[Rol, RolCreate, RolUpdate]):
    ...


rol_crud = UserCrud(Rol)