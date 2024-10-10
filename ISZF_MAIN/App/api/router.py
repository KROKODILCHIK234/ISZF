from fastapi import APIRouter
from .endpoints import items  # Корректный импорт эндпоинтов


router = APIRouter()

# Подключаем роутер с префиксом /items
router.include_router(items.router, prefix="/items", tags=["items"])
