"""
Модели данных для приложения.
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    """
    Модель пользователя
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __init__(self, username: str, email: str, password: str):
        """
        Конструктор для создания нового пользователя
        """
        self.username = username
        self.email = email
        self.password = password


class Post(Base):
    """
    Модель поста
    """
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="posts")

    def __init__(self, title: str, content: str, user_id: int):
        """
        Конструктор для создания нового поста.
        """
        self.title = title
        self.content = content
        self.user_id = user_id
