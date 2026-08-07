from typing import Optional
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseEntity


class SystemLog(BaseEntity):
    """
    SystemLog entity capturing application logs, errors, and diagnostic events.
    """
    __tablename__ = "system_logs"

    level: Mapped[str] = mapped_column(String(20), nullable=False, index=True)  # e.g., INFO, WARNING, ERROR
    module: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    stack_trace: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
