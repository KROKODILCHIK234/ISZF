from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

# SQLAlchemy модель
class OrderModel(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)

# Pydantic схемы
class OrderCreate(BaseModel):
    product_name: str
    quantity: int

class OrderRead(BaseModel):
    id: int
    product_name: str
    quantity: int

    class Config:
        orm_mode = True
