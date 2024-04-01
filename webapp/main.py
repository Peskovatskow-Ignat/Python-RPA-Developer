from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from webapp.api.v1.task.router import task_router
from webapp.migrate import migrate


def setup_routes(app: FastAPI) -> None:
    """Устанавливает маршруты для приложения FastAPI.

    Args:
        app (FastAPI): Экземпляр приложения FastAPI.
    """
    routers = [task_router]
    for router in routers:
        app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Асинхронный контекстный менеджер для жизненного цикла приложения FastAPI.

    Этот контекстный менеджер обрабатывает операции, которые должны быть выполнены при запуске и остановке приложения.

    Args:
        app (FastAPI): Экземпляр приложения FastAPI.

    Yields:
        AsyncIterator[None]: Асинхронный итератор, передающий управление обратно вызывающей стороне в течение жизненного цикла приложения.
    """
    await migrate()

    yield

    return


def create_app() -> FastAPI:
    """Создает экземпляр приложения FastAPI.

    Returns:
        FastAPI: Экземпляр приложения FastAPI.
    """
    app = FastAPI(docs_url='/swagger', lifespan=lifespan)
    setup_routes(app)
    return app
