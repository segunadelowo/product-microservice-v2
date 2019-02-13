import unittest
import datetime

from app.main import db
from app.main.model.category import Category
from app.test.base import BaseTestCase


class TestCategoryModel(BaseTestCase):

    def test_category_creation(self):
        category = Category(
            name='CATEGORY1',
            category_uuid='iu0809ihj'
        )
        db.session.add(category)
        db.session.commit()
        self.assertTrue(category.id > 0)


if __name__ == '__main__':
    unittest.main()