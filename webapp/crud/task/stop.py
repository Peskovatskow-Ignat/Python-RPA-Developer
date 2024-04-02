from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.integrations.celery_app.celery import app_celery
from webapp.models.enum.task import TaskStatus
from webapp.models.robot.task import Task


async def stop_task_by_id(session: AsyncSession, task_id: int) -> Task | None:
    """Останавливает задачу робота по ее идентификатору.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для взаимодействия с базой данных.
        task_id (int): Идентификатор задачи робота.

    Returns:
        Task | None: Задача робота или None, если задача не найдена или уже отозвана.
    """
    task = await session.get(Task, task_id)

    if not task or task.status == TaskStatus.revoked:
        return None

    task.status = TaskStatus.revoked
    task.work_time = int((datetime.now() - task.start_time).total_seconds())
    app_celery.control.revoke(
        f'{task_id}',
        terminate=True,
    )

    await session.commit()
    return task


async def stop_task(session: AsyncSession) -> Task | None:
    """Останавливает текущую запущенную задачу робота по очереди FIFO.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для взаимодействия с базой данных.

    Returns:
        Task | None: Задача робота или None, если нет запущенных задач.
    """

    task = await session.scalar(select(Task).where(Task.status == TaskStatus.launched))

    if not task:
        return None

    task.status = TaskStatus.revoked
    task.work_time = int((datetime.now() - task.start_time).total_seconds())
    app_celery.control.revoke(
        f'{task.id}',
        terminate=True,
    )

    await session.commit()
    return task
