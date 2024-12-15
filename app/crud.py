from sqlalchemy.orm import Session
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

# Обновление email пользователя
def update_user_email(db: Session, user_id: int, new_email: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
    return db_user

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
