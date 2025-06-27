from flask import Flask

from src.api.routes.categories import categories_blueprint
from src.api.routes.poll import polls_blueprint
from src.api.routes.vote import votes_blueprint


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(polls_blueprint)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(votes_blueprint)
