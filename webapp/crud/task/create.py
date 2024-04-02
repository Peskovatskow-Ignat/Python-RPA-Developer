from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.robot.task import Task


async def create_task(session: AsyncSession, start_number: int) -> Task:
    """Создает новую задачу робота и сохраняет ее в базу данных.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для взаимодействия с базой данных.
        start_number (int): Начальное значение для создаваемой задачи.

    Returns:
        Task: Созданная задача робота.
    """
    task = Task(start_number=start_number)

    async with session.begin_nested():
        session.add(task)
        await session.flush()
        await session.commit()

    return task
