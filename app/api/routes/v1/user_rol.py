from fastapi import APIRouter, Depends, HTTPException

from app.schemas.user_rol import UserRolCreate, UserRolInDB
from app.services.user_rol import user_rol_svc

router = APIRouter()

@router.post("", response_model= UserRolInDB, status_code=201)
def create_user_rol(*, new_user_rol: UserRolCreate ) -> UserRolInDB:
    return user_rol_svc.create(obj_in=new_user_rol)

@router.get("", response_model=list[UserRolInDB], status_code=200)
def get_all_rol(
    *, skip: int = 0, limit: int = 10
) -> list[UserRolInDB]:
    return  user_rol_svc.get_multi(skip=skip, limit=limit)