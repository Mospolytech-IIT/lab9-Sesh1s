"""
Схемы для валидации данных, передаваемых в API.
"""

from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel, EmailStr

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


# Схема для изменения e-mail
class UserUpdate(BaseModel):
    email: EmailStr

# Схема для изменения контента
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# Схема для ответа на запрос пользователя
class User(UserCreate):
    id: int

    class Config:
        from_attributes = True

# Схема для создания поста
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

# Схема для ответа на запрос поста
class Post(PostCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
