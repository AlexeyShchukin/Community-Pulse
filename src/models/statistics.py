from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import db
from src.models.base import BaseModel


class PollStatistic(BaseModel):
    __tablename__ = "poll_statistics"

    poll_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('polls.id'),
        unique=True,
        nullable=False
    )

    total_votes: Mapped[int] = mapped_column(
        db.Integer,
        default=0
    )
    unique_voters: Mapped[int] = mapped_column(
        db.Integer,
        default=0
    )

    # RELATIONS
    poll: Mapped['Poll'] = relationship(
        'Poll',
        back_populates='poll_stats',
    )

    option_stats: Mapped[list['OptionStatistic']] = relationship(
        'OptionStatistic',
        back_populates='poll_stats',
        cascade='all, delete-orphan',
    )


class OptionStatistic(BaseModel):
    __tablename__ = "option_statistics"

    poll_stats_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('poll_statistics.id'),
        nullable=False
    )

    option_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('poll_options.id'),
        nullable=False
    )

    votes_count: Mapped[int] = mapped_column(
        db.Integer,
        default=0
    )
    percentage: Mapped[float] = mapped_column(
        db.Float,
        default=0.0
    )

    # RELATIONS

    poll_stats: Mapped['PollStatistic'] = relationship(
        'PollStatistic',
        back_populates='option_stats',
    )
    poll_options: Mapped['PollOption'] = relationship(
        'PollOption',
        back_populates='option_stats',
    )
