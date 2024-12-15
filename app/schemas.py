"""
Схемы для валидации данных, передаваемых в API.
"""

from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Схема для создания пользователя
    """
    username: str
    email: str
    password: str


class PostCreate(BaseModel):
    """
    Схема для создания поста
    """
    title: str
    content: str
