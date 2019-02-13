from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key


class Category(db.Model):
    """ Category Model for storing Category related details """

    __tablename__ = 'categories'
 
    id = db.Column(db.Integer, primary_key=True)
    category_uuid = db.Column(db.String(80))
    name = db.Column(db.String(80))

    def __init__(self, category_uuid, name):
        self.category_uuid = category_uuid
        self.name = name

    def __repr__(self):
        return "<Category '{}'>".format(self.name)