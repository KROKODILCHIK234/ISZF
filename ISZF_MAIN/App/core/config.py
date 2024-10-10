import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

class Settings:
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploaded_files")

settings = Settings()
