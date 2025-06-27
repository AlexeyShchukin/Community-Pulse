from src.models.vote import Vote
from src.repositories.base import BaseRepository


class VoteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Vote)
