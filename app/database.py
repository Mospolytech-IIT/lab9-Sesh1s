"""
Модуль для настройки подключения к базе данных
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql+psycopg2://username:password@localhost/dbname"

# Настройки подключения и создание движка
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии
def get_db():
    """
    Получить сессию для работы с базой данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
