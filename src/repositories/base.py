from typing import Any, Type, TypeVar, Union, List

from sqlalchemy.exc import SQLAlchemyError

from src.core.db import db
from src.core.exceptions import DatabaseException, EntityNotFoundException
from src.models.base import BaseModel

Model = TypeVar('Model', bound=BaseModel)


class BaseRepository:
    def __init__(self, model_class: Type[Model]):
        self.model_class = model_class

    def create(self, data: dict[str, Any]) -> Union[Model, DatabaseException]:
        try:
            model = self.model_class(**data)
            db.session.add(model)
            db.session.commit()
            return model
        except SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseException(f"Ошибка создания {self.model_class.__name__}: {str(e)}")

    def get_by_id(self, model_id: int) -> Union[Model, EntityNotFoundException, DatabaseException]:
        try:
            instance = db.session.get(self.model_class, model_id)
            if not instance:
                return EntityNotFoundException(f"{self.model_class.__name__} с ID {model_id} не найден")
            return instance
        except SQLAlchemyError as e:
            return DatabaseException(f"Ошибка получения {self.model_class.__name__}: {str(e)}")

    def get_all(self) -> Union[List[Model], DatabaseException]:
        try:
            instances = db.session.query(self.model_class).all()
            return instances
        except SQLAlchemyError as e:
            return DatabaseException(f"Ошибка получения списка {self.model_class.__name__}: {str(e)}")

    def update(self, model_id: int, data: dict[str, Any]) -> Union[Model, EntityNotFoundException, DatabaseException]:
        try:
            instance = db.session.get(self.model_class, model_id)
            if not instance:
                return EntityNotFoundException(f"{self.model_class.__name__} с ID {model_id} не найден")

            for key, value in data.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)

            db.session.commit()
            return instance
        except SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseException(f"Ошибка обновления {self.model_class.__name__}: {str(e)}")

    def delete(self, model_id: int) -> Union[bool, EntityNotFoundException, DatabaseException]:
        try:
            instance = db.session.get(self.model_class, model_id)
            if not instance:
                return EntityNotFoundException(f"{self.model_class.__name__} с ID {model_id} не найден")

            db.session.delete(instance)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            return DatabaseException(f"Ошибка удаления {self.model_class.__name__}: {str(e)}")
