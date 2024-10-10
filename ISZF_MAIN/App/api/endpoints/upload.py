from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter()

@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    """
    Загрузка файла на сервер.
    """
    file_location = f"./uploaded_files/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename}
