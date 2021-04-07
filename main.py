import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.routes.base import router as api_router


def get_application() -> FastAPI:
    PROJECT_NAME = "fast-api-practice"
    DEBUG: bool = True
    VERSION = "0.0.1"

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    application.include_router(api_router)

    return application


app = get_application()
uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
