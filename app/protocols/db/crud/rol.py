from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.rol import Rol
from app.schemas.rol import RolCreate, RolUpdate


class CRUDRolProtocol(CRUDProtocol[Rol, RolCreate, RolUpdate]):
    ...