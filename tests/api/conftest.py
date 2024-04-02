import json
from datetime import datetime
from pathlib import Path
from typing import AsyncGenerator, List

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from webapp.integrations import postgres
from webapp.integrations.postgres import get_session
from webapp.models.meta import metadata


@pytest.fixture()
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Фикстура для создания асинхронного клиента FastAPI.

    Args:
        app (FastAPI): Экземпляр FastAPI.

    Returns:
        AsyncGenerator[AsyncClient, None]: Асинхронный клиент FastAPI.
    """
    async with AsyncClient(app=app, base_url='http://test.com') as client:
        yield client


@pytest.fixture()
async def db_session(app: FastAPI) -> AsyncGenerator[AsyncSession, None]:
    """Фикстура для создания асинхронной сессии SQLAlchemy.

    Args:
        app (FastAPI): Экземпляр FastAPI.

    Returns:
        AsyncGenerator[AsyncSession, None]: Асинхронная сессия SQLAlchemy.
    """
    async with postgres.engine.begin() as connection:
        session_maker = async_sessionmaker(bind=connection)
        session = session_maker()

        async def mocked_session() -> AsyncGenerator[AsyncSession, None]:
            yield session

        app.dependency_overrides[get_session] = mocked_session  # noqa

        yield session

        await connection.rollback()


@pytest.fixture()
async def _load_fixtures(db_session: AsyncSession, fixtures: List[Path]) -> None:
    """Фикстура для загрузки данных фикстур в базу данных.

    Args:
        db_session (AsyncSession): Асинхронная сессия SQLAlchemy.
        fixtures (List[Path]): Список путей к файлам с фикстурами.
    """
    for fixture in fixtures:
        fixture_path = Path(fixture)
        model = metadata.tables[fixture_path.stem]

        with open(fixture_path, 'r') as file:
            values = json.load(file)

        for model_obj in values:
            for key, val in model_obj.items():
                if 'start_time' == key:
                    model_obj[key] = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f').date()
        await db_session.execute(insert(model).values(values))
        await db_session.commit()

    return


@pytest.fixture()
async def _common_api_fixture(_load_fixtures: None) -> None:
    """Фикстура для предварительной настройки среды тестирования API.

    Args:
        _load_fixtures (None): Результат загрузки данных фикстур в базу данных.
    """
    return
