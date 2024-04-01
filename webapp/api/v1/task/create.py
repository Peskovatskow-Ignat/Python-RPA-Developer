from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.task.router import task_router
from webapp.crud.task.create import create_task
from webapp.integrations.postgres import get_session
from webapp.schema.robot.task import TaskPesp
from webapp.integrations.celery_app.tasks import start_robot


@task_router.post('', status_code=status.HTTP_201_CREATED, response_model=TaskPesp)
async def create(
    start_number: int,
    session: AsyncSession = Depends(get_session),
) -> TaskPesp:
    try:
        task = await create_task(session, start_number)
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    print(task, task)
    data = {
            'start':start_number,
            'task_id': task.id
    }
    start_robot.apply_async(args=(data,), task_id=f'{task.id}')
    
    return task
