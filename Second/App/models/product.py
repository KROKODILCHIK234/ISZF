from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database import Base

# SQLAlchemy модель
class ProductModel(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

# Pydantic схемы
class ProductCreate(BaseModel):
    name: str
    price: float

class ProductRead(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True
