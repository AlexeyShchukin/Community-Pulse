from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    db.init_app(app)

    from src.models import (
        User, Poll, PollOption, Vote,
        PollStatistic, OptionStatistic
    )

    # Инициализация Flask-Migrate
    migrate.init_app(app, db)