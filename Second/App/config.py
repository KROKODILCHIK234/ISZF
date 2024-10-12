import os

# URL базы данных (например, SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
