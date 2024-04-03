from fastapi import Depends, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.task.router import task_router
from webapp.crud.task.stop import stop_task, stop_task_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.robot.task import TaskPesp, TaskStop


@task_router.post('/stop/id', status_code=status.HTTP_200_OK, response_model=TaskPesp)
async def stop_by_id(
    body: TaskStop,
    session: AsyncSession = Depends(get_session),
) -> TaskPesp:
    """Останавливает задачу по идентификатору.

    Args:
        body (TaskStop): Данные для остановки задачи.
        session (AsyncSession, optional): Сессия базы данных. Defaults to Depends(get_session).

    Raises:
        HTTPException: В случае ошибки в запросе или обработке.

    Returns:
        TaskPesp: Модель остановленной задачи.
    """
    try:
        task = await stop_task_by_id(session, body.task_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return parse_obj_as(TaskPesp, task)


@task_router.post('/stop', status_code=status.HTTP_200_OK, response_model=TaskPesp)
async def stop(
    session: AsyncSession = Depends(get_session),
) -> TaskPesp:
    """Останавливает текущую задачу.

    Args:
        session (AsyncSession, optional): Сессия базы данных. Defaults to Depends(get_session).

    Raises:
        HTTPException: В случае ошибки в запросе или обработке.

    Returns:
        TaskPesp: Модель остановленной задачи.
    """
    try:
        task = await stop_task(session)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return parse_obj_as(TaskPesp, task)
