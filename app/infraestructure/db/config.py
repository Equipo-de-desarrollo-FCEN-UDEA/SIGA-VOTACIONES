from app.services.user import user_svc
from app.services.rol import rol_svc
from app.services.user_rol import user_rol_svc

from app.infraestructure.db.crud.user import user_crud
from app.infraestructure.db.crud.rol import rol_crud
from app.infraestructure.db.crud.user_rol import user_rol_crud
from app.infraestructure.db.utils.model import BaseModel
from app.infraestructure.db.utils import session



#En este archivo lo que hacemos en crear la session en la base de datos


def init_db() -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""

    # print(settings.DATABASE_URL)
    # register_tortoise(
    #     app,
    #     config=TORTOISE_ORM,
    #     generate_schemas=True,
    #     add_exception_handlers=True,
    # )
    BaseModel.metadata.create_all(bind=session.engine)
    user_svc.register_observer(user_crud)
    rol_svc.register_observer(rol_crud)
    user_rol_svc.register_observer(user_rol_crud)


# async def generate_schema() -> None:
#     log.info("Initializing Tortoise...")
#     await Tortoise.init(config=TORTOISE_ORM)
#     log.info("Generating database schema via Tortoise...")
#     await Tortoise.generate_schemas()