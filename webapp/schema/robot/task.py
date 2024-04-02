from datetime import datetime

from pydantic import BaseModel, ConfigDict

from webapp.models.enum.task import TaskStatus


class TaskPesp(BaseModel):
    """Модель которая возврвещается при создании, изменении и вывода задачи."""

    model_config = ConfigDict(from_attributes=True)

    id: int

    start_number: int

    start_time: datetime

    work_time: float | None

    status: TaskStatus


class TaskCreate(BaseModel):
    """Модель которая используется для создания задачи"""

    start_number: int


class TaskStop(BaseModel):
    """Модель которая используется для остановки задачи"""

    task_id: int
