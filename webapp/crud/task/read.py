from typing import Any, Coroutine

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.integrations.celery_app.celery import app_celery
from webapp.models.enum.task import TaskStatus
from webapp.models.robot.task import Task


async def get_all_tasks(sessions: AsyncSession) -> Coroutine:

    active_tasks = app_celery.control.inspect().active()

    return (await sessions.scalars(select(Task))).all()


async def get_tasks_by_status(session: AsyncSession, status: TaskStatus) -> Coroutine:

    return (await session.scalars(select(Task).where(Task.status == status))).all()
