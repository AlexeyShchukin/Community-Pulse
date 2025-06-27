from flask import Blueprint

from src.api.controllers.vote import VoteController
from src.core.config import settings

votes_blueprint = Blueprint(
    'votes',
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/votes"
)

vote_controller = VoteController()

votes_blueprint.add_url_rule(
    '',
    view_func=vote_controller.get_votes,
    methods=['GET']
)
