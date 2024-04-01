from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from webapp.api.v1.task.router import task_router
from webapp.migrate import migrate


def setup_routes(app: FastAPI) -> None:
    routers = [task_router]
    for router in routers:
        print(router)
        app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await migrate()

    yield

    return


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/swagger', lifespan=lifespan)
    setup_routes(app)
    return app
