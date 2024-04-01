from enum import Enum


class TaskStatus(Enum):

    launched: str = "launched"

    revoked: str = "revoked"
