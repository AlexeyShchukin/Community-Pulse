from http import HTTPStatus

from flask import jsonify, request

from src.core.exceptions import (
    CategoryNotFoundException,
    CategoryValidationException,
    CategoryDatabaseException,
    CategoryUpdateException,
    CategoryDeletionException,
    CustomBaseException
)
from src.services.category import CategoryService


class CategoryController:
    category_service = CategoryService()

    def create_category(self):
        data = request.get_json()

        if not data:
            return jsonify(
                {
                    "status": "error",
                    "message": "No data provided"
                }
            ), HTTPStatus.BAD_REQUEST  # 400

        result = self.category_service.create_category(data)

        if isinstance(result, CustomBaseException):
            return jsonify({
                "status": "error",
                "message": result.message
            }), HTTPStatus.BAD_REQUEST

        return jsonify({
            "status": "success",
            "data": result
        }), HTTPStatus.CREATED

    def get_category_by_id(self, category_id: int):
        result = self.category_service.get_category(category_id)

        if isinstance(result, CategoryNotFoundException):
            return jsonify({
                "status": "error",
                "message": result.message
            }), HTTPStatus.NOT_FOUND  # 404 для ненайденной сущности

        if isinstance(result, CategoryDatabaseException):
            return jsonify({
                "status": "error",
                "message": result.message
            }), HTTPStatus.INTERNAL_SERVER_ERROR  # 500 для ошибок базы данных

        return jsonify({
            "status": "success",
            "data": result
        }), HTTPStatus.OK  # 200

    def get_categories(self):
        result = self.category_service.get_all_categories()

        if isinstance(result, CategoryDatabaseException):
            return jsonify({
                "status": "error",
                "message": result.message
            }), HTTPStatus.INTERNAL_SERVER_ERROR  # 500

        return jsonify({
            "status": "success",
            "data": result
        }), HTTPStatus.OK

    def update_category(self, category_id: int):
        data = request.get_json()

        if not data:
            return jsonify(
                {
                    "status": "error",
                    "message": "No data provided"
                }
            ), HTTPStatus.BAD_REQUEST

        result = self.category_service.update_category(
            category_id=category_id,
            data=data
        )

        if isinstance(result, CategoryNotFoundException):
            return jsonify({
                "status": 'error',
                "message": result.message
            }), HTTPStatus.NOT_FOUND

        if isinstance(result, CategoryValidationException):  # Добавляем проверку на ошибку валидации из сервиса
            return jsonify({
                "status": 'error',
                "message": result.message
            }), HTTPStatus.BAD_REQUEST

        if isinstance(result, CategoryUpdateException):
            return jsonify({
                "status": 'error',
                "message": result.message
            }), HTTPStatus.INTERNAL_SERVER_ERROR  # Ошибка обновления, возможно, связана с БД

        return jsonify({
            "status": 'success',
            "data": result
        }), HTTPStatus.OK

    def delete_category(self, category_id: int):
        result = self.category_service.delete_category(category_id)

        if isinstance(result, CategoryNotFoundException):
            return jsonify({
                "status": 'error',
                "message": result.message
            }), HTTPStatus.NOT_FOUND

        if isinstance(result, CategoryDeletionException):
            return jsonify({
                "status": 'error',
                "message": result.message
            }), HTTPStatus.INTERNAL_SERVER_ERROR

        # В случае успеха (result == True), возвращаем 204 No Content
        return jsonify({
            "status": 'success',
            "message": "Category deleted successfully"
        }), HTTPStatus.NO_CONTENT