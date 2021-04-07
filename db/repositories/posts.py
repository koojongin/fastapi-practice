from fastapi import Depends
from sqlalchemy.orm import Session

from db.repositories.base import BaseRepository
from db.session import SessionLocal, get_db
from models.post import Post


class PostsRepository:

    async def get_post_by_id(self, db: Session) -> Post:
        data = db.query(Post).all()
        return data[0]

    async def get_posts(self, db: Session) -> None:
        return db.query(Post).offset(0).limit(10).all()
