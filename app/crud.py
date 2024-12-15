from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app import models, schemas
from . import models
from .models import User, Post

# Добавление нового пользователя
def add_user(db: Session, username: str, email: str, password: str):
    db_user = User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Добавление нового поста
def add_post(db: Session, title: str, content: str, user_id: int):
    db_post = Post(title=title, content=content, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Извлечение всех пользователей
def get_all_users(db: Session):
    return db.query(User).all()

# Извлечение всех постов
def get_all_posts(db: Session):
    return db.query(Post).all()

# Получение поста и пользователя по id
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

# Обновление контента
def update_post_content(db: Session, post_id: int, post: schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        if post.title is not None:
            db_post.title = post.title
        if post.content is not None:
            db_post.content = post.content
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

# Обновление email пользователя
def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return user
    return None

# Удаление поста
def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()

# Удаление пользователя и его постов
def delete_user_and_posts(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.query(Post).filter(Post.user_id == user_id).delete()
        db.delete(db_user)
        db.commit()
