from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel


class User(BaseModel):
    uid = Column(String(36), unique=True)
    email = Column(String(100), unique=True)
    names = Column(String(100), nullable=True)
    last_names = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    hashed_password = Column(String(300), nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    active = Column(Boolean, nullable=True, default=True)

    
    # rol = ForeignKeyField("Rol", related_name="user")
    # relations
   
    user_rol = relationship("UserRol", back_populates="user")
    
    # application_id = Column(Integer, ForeignKey("application.id"))
    # application = relationship("Application", back_populates="application_status")
    # status_id = Column(Integer, ForeignKey("status.id"))
    # status = relationship("Status", back_populates="application_status")
    
