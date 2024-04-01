from typing import Annotated, List

from fastapi import Depends, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.task.router import task_router
from webapp.crud.task.read import get_all_tasks, get_tasks_by_status
from webapp.integrations.postgres import get_session
from webapp.models.enum.task import TaskStatus
from webapp.schema.robot.task import TaskPesp


@task_router.get('', status_code=status.HTTP_200_OK, response_model=List[TaskPesp])
async def get_tasks(session: AsyncSession = Depends(get_session)) -> List[TaskPesp]:
    tasks = await get_all_tasks(session)

    return parse_obj_as(List[TaskPesp], tasks)


@task_router.get('/{status}', status_code=status.HTTP_200_OK, response_model=List[TaskPesp])
async def get_tasks(status: TaskStatus, session: AsyncSession = Depends(get_session)) -> List[TaskPesp]:
    tasks = await get_tasks_by_status(session, status)

    return parse_obj_as(List[TaskPesp], tasks)
