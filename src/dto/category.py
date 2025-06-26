from src.dto import BaseDTO


class CategoryRequestDTO(BaseDTO):
    name: str


class CategoryUpdateDTO(BaseDTO):
    name: str = None


class CategoryResponseDTO(BaseDTO):
    name: str
