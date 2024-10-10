from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# Модель для данных, передаваемых на /register
class RegisterRequest(BaseModel):
    id: int  # Ожидаемое поле - идентификатор пользователя

# Модель для данных, передаваемых на /send_data
class SendDataRequest(BaseModel):
    time: str  # Время в строковом формате для представления datetime
    geo_file: bytes  # Двоичный файл GEO
    VladimirAppFile: bytes  # Двоичный файл мобильного приложения Владимира
    status: str  # Статус обработки файлов


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}


# Обработка POST-запроса на /register
@app.post("/register")
async def register_user(data: RegisterRequest):
    """
    Регистрация пользователя по ID.
    Генерация RID на основе ID пользователя.
    
    :param data: объект RegisterRequest с полем id
    :return: сгенерированный RID
    """
    rid = data.id + 1000  # Пример генерации RID (идентификатор регистрации)
    return {"RID": rid}  # Возвращаем сгенерированный RID

# Обработка POST-запроса на /send_data
@app.post("/send_data")
async def send_data(data: SendDataRequest):
    """
    Получение данных о времени и двоичных файлах.
    Конвертация времени из строки в объект datetime.
    Возвращение статуса обработки файлов.
    
    :param data: объект SendDataRequest с полями time, geo_file, VladimirAppFile и status
    :return: идентификатор RID, статус и время
    """
    # Конвертируем строковое время обратно в datetime
    try:
        time_obj = datetime.strptime(data.time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format. Use YYYY-MM-DD HH:MM:SS")
    
    # Пример обработки данных
    rid = 12345  # Пример RID для отправки данных
    status = data.status  # Получаем статус обработки файлов

    # Пример логики обработки файлов (может быть адаптирована в зависимости от задачи)
    if not data.geo_file or not data.VladimirAppFile:
        raise HTTPException(status_code=400, detail="Both files must be provided")

    # Возвращаем данные
    return {
        "RID": rid,
        "status": status,
        "time_received": time_obj
    }

# маршрут для загрузки файлов
@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    """
    Обработка загрузки файла. Сохранение файла на сервере.
    
    :param file: загружаемый файл типа UploadFile
    :return: название сохраненного файла
    """
    file_location = f"./uploaded_files/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename}

# маршрут для получения списка загруженных файлов
@app.get("/files/")
async def list_files():
    """
    Возвращает список загруженных файлов на сервере.
    
    :return: список имен файлов
    """
    files = os.listdir("./uploaded_files")
    return {"files": files}

# маршрут для получения информации о системе
@app.get("/status/")
async def get_status():
    """
    Возвращает текущий статус сервера, включая системную дату и время.
    
    :return: статус сервера c датой и временем
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {"status": "running", "current_time": current_time}
    return {
        "RID": rid,
        "status": status,
        "time_received": time_obj,
        "files": {
            "geo_file": "received" if data.geo_file else "not received",
            "VladimirAppFile": "received" if data.VladimirAppFile else "not received"
        }
    }