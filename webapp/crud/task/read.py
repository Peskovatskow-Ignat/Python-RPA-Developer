from typing import Any, Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.robot.task import Task


async def get_all_tasks(session: AsyncSession) -> Sequence[Task]:
    """Возвращает все задачи робота из базы данных.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для взаимодействия с базой данных.

    Returns:
        Sequence[Task]: Последовательность задач робота.
    """
    return (await session.scalars(select(Task))).all()


async def get_tasks_by_id(session: AsyncSession, task_id: int) -> Coroutine[Any, Any, Any] | None:
    """Возвращает задачу робота по ее идентификатору.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для взаимодействия с базой данных.
        task_id (int): Идентификатор задачи робота.

    Returns:
        Coroutine[Any, Any, Any] | None: Асинхронный результат запроса или None, если задача не найдена.
    """
    return await session.get(Task, task_id)
