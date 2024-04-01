from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.robot.task import Task
from webapp.models.enum.task import TaskStatus


async def stop_task_by_id(session: AsyncSession, task_id: int) -> Task:

    task = await session.get(Task, task_id)

    setattr(task, 'status', TaskStatus.completed)
    setattr(task)

    await session.commit()
    
    return task