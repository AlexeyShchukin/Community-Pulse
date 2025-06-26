from src.models.poll import Category
from src.repositories.base import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)
