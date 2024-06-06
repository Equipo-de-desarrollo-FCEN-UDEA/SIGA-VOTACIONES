from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import UserRol
from app.schemas.user_rol import UserRolCreate, UserRolUpdate

class UserRolCrud(CRUDBase[UserRol, UserRolCreate, UserRolUpdate]):
    ...
    
user_rol_crud = UserRolCrud(UserRol)