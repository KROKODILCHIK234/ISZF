from fastapi import FastAPI
from routes.api import api_router
from database import engine, Base

app = FastAPI()

# Создание всех таблиц в базе данных при запуске
Base.metadata.create_all(bind=engine)

# Подключение роутеров
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ISZF API"}
