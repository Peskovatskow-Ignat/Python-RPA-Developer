import pytest
from sqlalchemy import create_engine
from typing import AsyncGenerator

from sqlalchemy import QueuePool
from sqlalchemy.ext.asyncio import create_async_engine
from webapp.models import meta
import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncGenerator
from fastapi import FastAPI
from webapp.main import create_app

@pytest.fixture(scope='session')
async def app(_migrate_db: None) -> FastAPI:
    return create_app()


@pytest.fixture(scope='session')
def event_loop() -> AbstractEventLoop:
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
async def _migrate_db() -> AsyncGenerator[None, None]:
    engine = create_async_engine(
        'postgresql+asyncpg://postgres:postgres@test_db:4444/test_db',
        poolclass=QueuePool,
        connect_args={
            'statement_cache_size': 0,
        },
    )
    # engine = create_engine('postgresql+asyncpg://postgres:postgres@test_db:5432/test_db')

    async with engine.begin() as conn:
        conn.run_sync(meta.metadata.create_all)

    yield

    async with engine.begin() as conn:
        conn.run_sync(meta.metadata.drop_all)
        