from typing import AsyncGenerator

from sqlalchemy import QueuePool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine


def create_engine() -> AsyncEngine:
    """Создает асинхронный движок для работы с базой данных.

    Returns:
        AsyncEngine: Асинхронный движок SQLAlchemy.
    """
    return create_async_engine(
        'postgresql+asyncpg://postgres:postgres@web_db:5432/main_db',
        poolclass=QueuePool,
        connect_args={
            'statement_cache_size': 0,
        },
    )


def create_session(engine: AsyncEngine | None = None) -> async_sessionmaker[AsyncSession]:
    """Создает асинхронную сессию для работы с базой данных.

    Args:
        engine (AsyncEngine | None, optional): Асинхронный движок SQLAlchemy. Defaults to None.

    Returns:
        async_sessionmaker[AsyncSession]: Асинхронная сессия SQLAlchemy.
    """
    return async_sessionmaker(
        bind=engine or create_engine(),
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
    )


engine = create_engine()
async_session = create_session(engine)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Генератор асинхронных сессий для работы с базой данных.

    Returns:
        AsyncGenerator[AsyncSession, None]: Генератор асинхронных сессий SQLAlchemy.
    """
    async with async_session() as session:
        yield session
