from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

# Создаем роутер для элементов
router = APIRouter()

# Модель элемента
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# Пример базы данных
items_db = [
    {"id": 1, "name": "Item 1", "description": "Description 1"},
    {"id": 2, "name": "Item 2", "description": "Description 2"},
]

# Маршрут для получения всех элементов
@router.get("/", response_model=List[Item])
async def get_items():
    return items_db

# Маршрут для получения элемента по ID
@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
