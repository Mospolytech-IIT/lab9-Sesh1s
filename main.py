"""
Основной файл для запуска FastAPI приложения.

Этот модуль содержит маршруты и обработчики для взаимодействия с базой данных через API.
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, models, database

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Создать нового пользователя
    """
    return crud.add_user(db, user.username, user.email, user.password)


@app.post("/posts/")
def create_post(post: schemas.PostCreate, user_id: int, db: Session = Depends(database.get_db)):
    """
    Создать новый пост
    """
    return crud.add_post(db, post.title, post.content, user_id)


@app.get("/users/")
def get_users(db: Session = Depends(database.get_db)):
    """
    Получить всех пользователей
    """
    return crud.get_all_users(db)


@app.get("/posts/")
def get_posts(db: Session = Depends(database.get_db)):
    """
    Получить все посты
    """
    return crud.get_all_posts(db)


@app.put("/users/{user_id}/")
def update_user(user_id: int, email: str, db: Session = Depends(database.get_db)):
    """
    Обновить email пользователя
    """
    return crud.update_user_email(db, user_id, email)


@app.put("/posts/{post_id}/")
def update_post(post_id: int, content: str, db: Session = Depends(database.get_db)):
    """
    Обновить контент поста
    """
    return crud.update_post_content(db, post_id, content)


@app.delete("/posts/{post_id}/")
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    """
    Удалить пост
    """
    crud.delete_post(db, post_id)
    return {"message": "Post deleted"}


@app.delete("/users/{user_id}/")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    """
    Удалить пользователя и все его посты
    """
    crud.delete_user_and_posts(db, user_id)
    return {"message": "User and their posts deleted"}
