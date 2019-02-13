from flask import request
from flask_restplus import Resource

from ..dto.category_dto import CategoryDto
from ..service.category_service import save_new_category, get_all_categories, find_by_name,find_by_id,find_by_uuid

api = CategoryDto.api
_category = CategoryDto


@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_categories')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all categories"""
        return get_all_categories()

    @api.response(201, 'category successfully created.')
    @api.doc('create a new category')
    @api.expect(_category, validate=True)
    def post(self):
        """Creates a new category """
        data = request.json
        return save_new_category(data=data)


@api.route('/<category_uuid>')
@api.param('category_uuid', 'The category identifier')
@api.response(404, 'category not found.')
class Category(Resource):
    @api.doc('get a category')
    @api.marshal_with(_category)
    def get(self, public_id):
        """get a category given its identifier"""
        Category = find_by_uuid(public_id)
        if not category:
            api.abort(404)
        else:
            return category