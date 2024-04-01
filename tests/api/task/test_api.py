from pathlib import Path

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from tests.conf import URLS

from webapp.models.robot.task import Task

BASE_DIR = Path(__file__).parent
FIXTURES_PATH = BASE_DIR / 'fixtures'


@pytest.mark.asyncio()
# @pytest.mark.usefixtures('_common_api_fixture')
async def test_test(client: AsyncClient, db_session: AsyncSession):
    assert 1 == 1