from typing import Coroutine

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.robot.task import Task


async def get_all_tasks(sessions: AsyncSession) -> Coroutine:

    return (await sessions.scalars(select(Task))).all()


async def get_tasks_by_id(session: AsyncSession, task_id: int) -> Coroutine:

    return await session.get(Task, task_id)
