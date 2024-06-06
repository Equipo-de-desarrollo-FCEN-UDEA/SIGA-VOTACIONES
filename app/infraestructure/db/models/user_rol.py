from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel



class UserRol(BaseModel):
    
    observation = Column(String(100), unique=False)
    
    #Relations
    
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates ="user_rol")
    rol_id = Column(Integer, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="user_rol")
    
    