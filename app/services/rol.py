from app.services.base import ServiceBase
from app.schemas.rol import RolCreate, RolUpdate
from app.protocols.db.models.rol import Rol
from app.protocols.db.crud.rol import CRUDRolProtocol

class RolService(ServiceBase[Rol, RolCreate, RolUpdate, CRUDRolProtocol]):
    ...


rol_svc = RolService()