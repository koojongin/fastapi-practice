from fastapi import APIRouter

from api.routes import posts

router = APIRouter()
router.include_router(posts.router, tags=["post"], prefix="/posts")
