from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.robot.task import Task


async def create_task(session: AsyncSession, start_number: int) -> Task:

    task = Task(start_number=start_number)

    async with session.begin_nested():
        session.add(task)
        await session.flush()
        await session.commit()

    return task
