from typing import Annotated, List

from fastapi import Depends, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.crud.task.read import get_all_tasks
from webapp.integrations.postgres import get_session
from webapp.schema.robot.task import TaskPesp
from webapp.api.v1.task.router import task_router



@task_router.get('', status_code=status.HTTP_200_OK, response_model=List[TaskPesp])
async def get_tasks(session: AsyncSession = Depends(get_session)) -> List[TaskPesp]:
    tasks = await get_all_tasks(session)
    print
    return parse_obj_as(List[TaskPesp], tasks)