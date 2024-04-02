from enum import Enum


class TaskStatus(Enum):
    """Перечисляет возможные статусы задачи."""

    launched: str = "launched"

    revoked: str = "revoked"
