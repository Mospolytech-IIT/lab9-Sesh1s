from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models, database
from app.database import engine, Base
from app import models

app = FastAPI()

# Создать таблицы в бд
Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Создать нового пользователя
    """
    return crud.add_user(db, user.username, user.email, user.password)


@app.post("/posts/")
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    """
    Создать новый пост
    """
    return crud.add_post(db, post.title, post.content, post.user_id)


@app.get("/users/", response_model=list[schemas.User])
def get_users(db: Session = Depends(database.get_db)):
    """
    Получить всех пользователей
    """
    return crud.get_all_users(db)


@app.get("/posts/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(database.get_db)):
    """
    Получить все посты
    """
    return crud.get_all_posts(db)

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    """
    Получить пользователя по ID
    """
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/posts/{post_id}", response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(database.get_db)):
    """
    Получить пост по ID
    """
    post = crud.get_post_by_id(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/users/{user_id}/", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    """
    Обновить email пользователя
    """
    updated_user = crud.update_user_email(db, user_id, user.email)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(database.get_db)):
    """
    Обновить контент поста
    """
    updated_post = crud.update_post_content(db, post_id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    """
    Удалить пост
    """
    crud.delete_post(db, post_id)
    return {"message": "Post deleted"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    """
    Удалить пользователя и все его посты
    """
    crud.delete_user_and_posts(db, user_id)
    return {"message": "User and their posts deleted"}
