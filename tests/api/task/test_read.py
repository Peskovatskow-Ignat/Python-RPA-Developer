from pathlib import Path

import loguru
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from tests.conf import URLS

BASE_DIR = Path(__file__).parent
FIXTURES_PATH = BASE_DIR / 'fixtures'


@pytest.mark.parametrize(
    ('expected_status'),
    [status.HTTP_200_OK],
)
@pytest.mark.asyncio()
async def test_read(client: AsyncClient, db_session: AsyncSession, expected_status: int) -> None:
    """Тест чтения всех данных

    Args:
        client (AsyncClient): Асинхронный клиент для отправки запросов.
        db_session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.
        expected_status (int): Ожидаемый статус ответа.

    Returns:
        None
    """
    loguru.logger.info(db_session)

    response = await client.get(URLS['api']['v1']['task'])

    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ('task_id', 'expected_status', 'fixtures'),
    [
        (0, status.HTTP_200_OK, [FIXTURES_PATH / 'robot.task.json']),
        (999, status.HTTP_404_NOT_FOUND, [FIXTURES_PATH / 'robot.task.json']),
    ],
)
@pytest.mark.asyncio()
@pytest.mark.usefixtures('_common_api_fixture')
async def test_read_by_id(client: AsyncClient, db_session: AsyncSession, task_id: int, expected_status: int) -> None:
    """Тест чтения данных из API по конкретному идентификатору задачи.

    Args:
        client (AsyncClient): Асинхронный клиент для отправки запросов.
        db_session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.
        task_id (int): Идентификатор задачи.
        expected_status (int): Ожидаемый статус ответа.

    Returns:
        None
    """

    response = await client.get(''.join([URLS['api']['v1']['task'], '/', str(task_id)]))

    assert response.status_code == expected_status
