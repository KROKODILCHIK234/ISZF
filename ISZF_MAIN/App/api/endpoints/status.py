from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status/")
async def get_status():
    """
    Возвращает текущий статус сервера.
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {"status": "running", "current_time": current_time}
