from enum import Enum

from sqlalchemy.orm import Mapped


class TaskStatus(Enum):

    launched: Mapped[str] = "launched"

    completed: Mapped[str] = "completed"
