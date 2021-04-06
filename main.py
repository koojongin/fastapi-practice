from typing import Optional
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.session import SessionLocal
from api.routes.base import router as api_router


def get_application() -> FastAPI:
    PROJECT_NAME = "fast-api-practice"
    DEBUG: bool = 1
    VERSION = "0.0.1"

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origin=["*"],
    #     allow_headers=["*"]
    # )

    application.include_router(api_router)
    return application


app = get_application()
