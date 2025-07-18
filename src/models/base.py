from datetime import datetime
from typing import Any
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import db


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        db.DateTime,
        default=datetime.now,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )


class BaseModel(db.Model, TimestampMixin):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
        }