from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.schemas import SendDataRequest

router = APIRouter()

@router.post("/send_data")
async def send_data(data: SendDataRequest):
    """
    Получение времени и файлов. Конвертация времени в объект datetime.
    """
    try:
        time_obj = datetime.strptime(data.time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format. Use YYYY-MM-DD HH:MM:SS")
    
    if not data.geo_file or not data.VladimirAppFile:
        raise HTTPException(status_code=400, detail="Both files must be provided")
    
    rid = 12345
    status = data.status

    return {
        "RID": rid,
        "status": status,
        "time_received": time_obj,
        "files": {
            "geo_file": "received",
            "VladimirAppFile": "received"
        }
    }
