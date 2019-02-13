import uuid
import datetime

from app.main import db
from app.main.model.category import Category


def save_new_category(data):
    category = Category.query.filter_by(email=data['email']).first()
    if not category:
        new_category = Category(
            category_uuid=str(uuid.uuid4()),
            name=data['name']
        )
        try:
            save_changes(new_category)
        except:
            return {'status': 'failed',
                    'message':"An error occurred while creating the Category."}, 500
        response_object = {
            'status': 'success',
            'message': 'Successfully Created.'
        }
        return response_object, 201


def get_all_categories():
    return Category.query.all()


def find_by_name(name): # cls is used instead of self, this points to the current class
    return Category.query.filter_by(name=name).first()


def find_by_id(_id): # cls is used instead of self, this points to the current class
    return Category.query.filter_by(id=_id).first()


def find_by_uuid(category_uuid): # cls is used instead of self, this points to the current class
    return Category.query.filter_by(category_uuid=category_uuid).first() 


def save_changes(data):
    db.session.add(data)
    db.session.commit()