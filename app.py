from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from schemas import UserGet
from schemas import PostGet
from schemas import FeedGet

from db_app.database import SessionLocal
from table_user import User
from table_post import Post
from feed_action_table import Feed


app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    response = db.query(User).filter(User.id==id).one_or_none()

    if response is None:
        print(response is None)
        raise HTTPException(404, f'No one user with id:{id}')

    return response


@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    response = db.query(Post).filter(Post.id==id).one_or_none()

    if response is None:
        print(response is None)
        raise HTTPException(404, f'No one post with{id}')

    return response


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    response = (
        db.query(Feed)
        .filter(Feed.user_id==id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )
    return response


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    response = (
        db.query(Feed)
        .filter(Feed.post_id==id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )
    return response


