from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repositories.posts import PostsRepository
from db.session import get_db
from models.post import Post

router = APIRouter()



@router.get("", name="posts:get")
async def get_post(
        db: Session = Depends(get_db),
):
    post = await PostsRepository().get_post_by_id(db)
    # post = db.query(Post).all()
    return post
