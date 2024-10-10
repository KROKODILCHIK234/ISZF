from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, ItemModel
from pydantic import BaseModel
from typing import List, Optional

# Определяем модель для API
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

router = APIRouter()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemModel(id=item.id, name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(ItemModel).offset(skip).limit(limit).all()

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item
