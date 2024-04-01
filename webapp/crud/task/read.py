from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.robot.task import Task


async def get_all_tasks(sessions: AsyncSession) -> Sequence[Task]:
    return (await sessions.scalars(select(Task))).all()


async def get_tasks_by_id(session: AsyncSession, task_id: int) -> Coroutine[Any, Any, Any] | None:
    return await session.get(Task, task_id)
