from flask import Blueprint

from src.api.controllers.category import CategoryController
from src.core.config import settings

categories_blueprint = Blueprint(
    'categories',
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/categories"
)

category_controller = CategoryController()

categories_blueprint.add_url_rule(
    '',
    view_func=category_controller.get_categories,
    methods=['GET']
)

categories_blueprint.add_url_rule(
    '',
    view_func=category_controller.create_category,
    methods=['POST']
)

categories_blueprint.add_url_rule(
    '/<int:category_id>',
    view_func=category_controller.get_category_by_id,
    methods=['GET']
)

categories_blueprint.add_url_rule(
    '/<int:category_id>',
    view_func=category_controller.update_category,
    methods=['PUT', 'PATCH']
)

categories_blueprint.add_url_rule(
    '/<int:category_id>',
    view_func=category_controller.delete_category,
    methods=['DELETE']
)
