from fastapi import APIRouter
from App.models.schemas import RegisterRequest

router = APIRouter()

@router.post("/register")
async def register_user(data: RegisterRequest):
    """
    Регистрация пользователя по ID и генерация RID.
    """
    rid = data.id + 1000  # Пример генерации RID на основе ID
    return {"RID": rid}
