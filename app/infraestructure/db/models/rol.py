from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel


class Rol(BaseModel):
    name= Column(String(100), nullable=True)
    description = Column(String(100), nullable=True)
    
    # relations
    user_rol = relationship ("UserRol", back_populates="rol")
    