from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from api.routers import ROUTER
from utils.exception_handlers import unknown_exception_handler


def add_exceptions(app: FastAPI):
    app.add_exception_handler(Exception, unknown_exception_handler)


def include_routers(app: FastAPI):
    app.include_router(ROUTER)


def add_middlewares(app: FastAPI):
    # cors for frontend
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["classes"]
    )


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api'
    )

    add_exceptions(app)
    add_middlewares(app)
    include_routers(app)

    return app
