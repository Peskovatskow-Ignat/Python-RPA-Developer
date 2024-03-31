from sqlalchemy import BigInteger, DateTime, Enum
from datetime import datetime
from webapp.models.enum.task import TaskStatus


from sqlalchemy.orm import Mapped, mapped_column

from webapp.models.robot.meta import Base


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    start_number: Mapped[int] = mapped_column(BigInteger, nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    work_time: Mapped[int] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(Enum(TaskStatus))