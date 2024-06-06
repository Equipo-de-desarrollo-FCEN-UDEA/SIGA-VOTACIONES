from fastapi import APIRouter, Depends, HTTPException

from app.schemas.rol import RolInDB 
from app.services.rol import rol_svc

router = APIRouter()

@router.get("", response_model=list[RolInDB], status_code=200)
def get_all_rol(
    *, skip: int = 0, limit: int = 10
) -> list[RolInDB]:
    return  rol_svc.get_multi(skip=skip, limit=limit)

@router.delete("/{id}", response_model=None, status_code=204)
def delete_user(*, id: int) -> None:
    user = rol_svc.delete(id=id)
    if user == 0:
        raise HTTPException(404, "User not found")
    return None