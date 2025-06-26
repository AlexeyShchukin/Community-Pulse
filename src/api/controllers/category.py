from http import HTTPStatus

from flask import jsonify, request

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

        category, err = self.category_service.create_category(data)

        if err:
            return jsonify({
                "status": "error",
                "message": err
            }), HTTPStatus.BAD_REQUEST

        return jsonify({
            "status": "success",
            "data": category
        }), HTTPStatus.CREATED

    def get_category_by_id(self, category_id: int):
        category, err = self.category_service.get_category(category_id)

        if err:
            return jsonify({
                "status": "error",
                "message": err
            }), HTTPStatus.NOT_FOUND if err == "Not found" else HTTPStatus.BAD_REQUEST

        return jsonify({
            "status": "success",
            "data": category
        }), HTTPStatus.OK  # 200

    def get_categories(self):
        categories, err = self.category_service.get_all_categories()

        if err:
            return jsonify({
                "status": "error",
                "message": err
            }), HTTPStatus.INTERNAL_SERVER_ERROR  # 500

        return jsonify({
            "status": "success",
            "data": categories
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

        category, err = self.category_service.update_category(
            category_id=category_id,
            data=data
        )

        if err:
            return (jsonify({
                "status": 'error',
                "message": err
            }), HTTPStatus.NOT_FOUND if err == f"{self.category_service.category_repo.model_class.__name__} not found"
            else HTTPStatus.BAD_REQUEST)

        return jsonify({
            "status": 'success',
            "data": category
        }), HTTPStatus.OK

    def delete_category(self, category_id: int):
        success, err = self.category_service.delete_category(category_id)

        if err:
            return (jsonify({
                "status": 'error',
                "message": err
            }), HTTPStatus.NOT_FOUND if err == f"{self.category_service.category_repo.model_class.__name__} not found"
            else HTTPStatus.BAD_REQUEST)

        return jsonify({
            "status": 'success',
        }), HTTPStatus.NO_CONTENT
