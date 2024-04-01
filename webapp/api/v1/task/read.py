from typing import List

from fastapi import Depends, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.task.router import task_router
from webapp.crud.task.read import get_all_tasks, get_tasks_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.robot.task import TaskPesp


@task_router.get('', status_code=status.HTTP_200_OK, response_model=List[TaskPesp])
async def get_tasks_all(session: AsyncSession = Depends(get_session)) -> List[TaskPesp]:
    tasks = await get_all_tasks(session)

    return parse_obj_as(List[TaskPesp], tasks)


@task_router.get('/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskPesp)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)) -> TaskPesp:
    task = await get_tasks_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return parse_obj_as(TaskPesp, task)
