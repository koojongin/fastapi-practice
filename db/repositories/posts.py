from fastapi import Depends
from sqlalchemy.orm import Session

from db import session
from models.post import Post

db: Session = Depends(session.get_db)


class PostsRepository:

    async def get_post(self) -> Post:
        return db.query(Post).offset(0).limit(1).all();

    async def get_posts(self) -> Post.Array:
        return db.query(Post).offset(0).limit(1).all();
