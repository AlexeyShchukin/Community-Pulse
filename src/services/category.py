from typing import List, Dict, Any, Union

from src.repositories.category import CategoryRepository

from src.dto import (
    CategoryRequestDTO,
    CategoryUpdateDTO,
    CategoryResponseDTO
)
from src.core.exceptions import (
    CustomBaseException,
    EntityNotFoundException,
    DatabaseException,
    CategoryNotFoundException,
    CategoryValidationException,
    CategoryDatabaseException,
    CategoryCreationException,
    CategoryUpdateException,
    CategoryDeletionException
)


class CategoryService:
    category_repository = CategoryRepository()

    def create_category(self, data: Dict[str, Any]) -> Union[Dict, CustomBaseException]:
        try:
            category_dto = CategoryRequestDTO(**data)

            result = self.category_repository.create(category_dto.model_dump())

            if isinstance(result, DatabaseException):
                return CategoryCreationException(result.message)

            category_response = CategoryResponseDTO.model_validate(result)
            return category_response.model_dump(mode='json')

        except Exception as e:
            return CategoryValidationException(f"Ошибка валидации при создании категории: {str(e)}")

    def get_category(self, category_id: int) -> Union[Dict, CustomBaseException]:
        result = self.category_repository.get_by_id(category_id)

        if isinstance(result, EntityNotFoundException):
            return CategoryNotFoundException(result.message)
        if isinstance(result, DatabaseException):
            return CategoryDatabaseException(result.message)

        category_response = CategoryResponseDTO.model_validate(result)
        return category_response.model_dump(mode='json')

    def get_all_categories(self) -> Union[List[Dict], CustomBaseException]:
        result = self.category_repository.get_all()

        if isinstance(result, DatabaseException):
            return CategoryDatabaseException(result.message)

        categories_list = [CategoryResponseDTO.model_validate(category).model_dump(mode='json')
                           for category in result]
        return categories_list

    def update_category(self, category_id: int, data: Dict[str, Any]) -> Union[Dict, CustomBaseException]:
        try:
            category_dto = CategoryUpdateDTO(**data)

            update_data = category_dto.model_dump(exclude_unset=True, exclude_none=True)

            if not update_data:
                return CategoryValidationException("Нет данных для обновления категории")

            result = self.category_repository.update(category_id, update_data)

            if isinstance(result, EntityNotFoundException):
                return CategoryNotFoundException(result.message)
            if isinstance(result, DatabaseException):
                return CategoryUpdateException(result.message)

            category_response = CategoryResponseDTO.model_validate(result)
            return category_response.model_dump(mode='json')

        except Exception as e:
            return CategoryValidationException(f"Ошибка валидации при обновлении категории: {str(e)}")

    def delete_category(self, category_id: int) -> Union[bool, CustomBaseException]:
        result = self.category_repository.delete(category_id)

        if isinstance(result, EntityNotFoundException):
            return CategoryNotFoundException(result.message)
        if isinstance(result, DatabaseException):
            return CategoryDeletionException(result.message)

        return result
