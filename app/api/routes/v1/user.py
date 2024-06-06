from fastapi import APIRouter, Depends, HTTPException
from app.errors.base import BaseErrors

from app.schemas.user import UserCreate, UserUpdate, UserInDB, UserSearch
from app.schemas.user_rol import UserRolCreate
from app.services.user import user_svc
from app.services.user_rol import user_rol_svc


router = APIRouter()


@router.post("", response_model=UserInDB, status_code=201)
def create_user(*, new_user: UserCreate, rol_id: str) -> UserInDB:
    """Endpoint to create a new user in db

    Args:
        new_user (UserCreate): Schema

    Returns:
        UserInDB: User in DB schema
    """
    # try:

    #     raise HTTPException(status_code=e.code, detail=e.detail)
    # except KeyError as e:
    #     raise HTTPException(status_code=422, detail=str(e))
    # except ValueError as e:
    #     raise HTTPException(status_code=422, detail=str(e))
    user = user_svc.create(obj_in=new_user)
    user_rol_svc.create(
        obj_in=UserRolCreate(
            rol_id=rol_id, user_id= user.id, observation="Se creó el usuario"))
    return user



@router.get("", response_model=list[UserInDB], status_code=200)
def get_all_user(
    *, skip: int = 0, limit: int = 10, payload: UserSearch = Depends()
) -> list[UserInDB]:
    return user_svc.get_multi(skip=skip, limit=limit, payload=payload.dict(exclude_none=True))


@router.get("/{id}", response_model=UserInDB, status_code=200)
def get_user(*, id: int) -> UserInDB:
    user = user_svc.get(id=id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.patch("/{id}", response_model=None)
def update_user(*, obj_in: UserUpdate, id: int) -> None:
    user = user_svc.get(id=id)
    if not user:
        raise HTTPException(404, "User not found")
    user_svc.update(id=id, obj_in=obj_in)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_user(*, id: int) -> None:
    user = user_svc.delete(id=id)
    if user == 0:
        raise HTTPException(404, "User not found")
    return None
