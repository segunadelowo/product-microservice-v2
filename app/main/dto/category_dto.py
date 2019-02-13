from flask_restplus import Namespace, fields

class CategoryDto:
    api = Namespace('category', description='category related operations')
    user = api.model('category', {
        'name': fields.String(required=True, description='category name'),
        'category_uuid': fields.String(description='category Identifier')
})