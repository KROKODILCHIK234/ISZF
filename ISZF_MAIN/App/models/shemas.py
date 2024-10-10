from pydantic import BaseModel
from typing import Optional

class RegisterRequest(BaseModel):
    id: int  # Идентификатор пользователя

class SendDataRequest(BaseModel):
    time: str  # Время в строковом формате
    geo_file: bytes  # Двоичный файл GEO
    VladimirAppFile: bytes  # Двоичный файл мобильного приложения Владимира
    status: str  # Статус обработки файлов
