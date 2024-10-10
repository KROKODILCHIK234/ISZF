from fastapi import FastAPI
from App.api.router import router

# Создаем экземпляр FastAPI
app = FastAPI()

# Подключаем роутеры
#app.include_router(router)

# Корневой маршрут для проверки, что приложение работает
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
