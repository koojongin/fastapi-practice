from fastapi import APIRouter

from models.post import Post

router = APIRouter()


@router.get("", name="posts:get")
async def get_post():
    return 1;
