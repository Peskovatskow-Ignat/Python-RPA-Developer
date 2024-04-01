from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column

from webapp.models.enum.task import TaskStatus
from webapp.models.meta import Base


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, nullable=False)

    start_number: Mapped[int] = mapped_column(BigInteger, nullable=False)

    start_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    work_time: Mapped[int] = mapped_column(BigInteger, nullable=True, default=None)

    status: Mapped[str] = mapped_column(Enum(TaskStatus), default=TaskStatus.launched)
