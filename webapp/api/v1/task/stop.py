from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.task.router import task_router
from webapp.crud.task.stop import stop_task_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.robot.task import TaskPesp


@task_router.patch('', status_code=status.HTTP_200_OK, response_model=TaskPesp)
async def stop(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> TaskPesp:
    try:
        task = await stop_task_by_id(session, id)
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    return task
