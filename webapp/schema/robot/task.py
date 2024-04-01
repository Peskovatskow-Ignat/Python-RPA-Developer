from datetime import datetime

from pydantic import BaseModel, ConfigDict

from webapp.models.enum.task import TaskStatus

class TaskPesp(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    start_number: int

    start_time: datetime

    work_time: int | None

    status: TaskStatus
