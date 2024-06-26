import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI

from webapp.integrations import postgres
from webapp.main import create_app
from webapp.models import meta


@pytest.fixture(scope='session')
async def app(_migrate_db: None) -> FastAPI:
    return create_app()


@pytest.fixture(scope='session')
def event_loop() -> AbstractEventLoop:
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
async def _migrate_db() -> AsyncGenerator[None, None]:
    async with postgres.engine.begin() as conn:
        await conn.run_sync(meta.metadata.create_all)

    yield

    async with postgres.engine.begin() as conn:
        await conn.run_sync(meta.metadata.drop_all)
