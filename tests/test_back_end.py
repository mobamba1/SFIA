import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Adding, User
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLACHEMY_DATABASE_URI=getenv('TEST_DATABASE'),
                SECRET_KEY=getenv('SKEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app










class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addpage_view(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)

    def test_removepage_view(self):
        response = self.client.get('/remove', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class TestAdding(TestBase):
    def test_add(self):
        with self.client:
            response = self.client.post(
                    '/add',
                    data=dict(
                        burnt=100,
                        intake=100
                    ),
                    follow_redirects=True
                    )
            self.assertIn(100,response.data)

    def test_add_loads(self):
        response = self.client.get('/add', content_type='html/text')
        self.assertTrue(b'Caloric Intake' in response.data)


class TestRemove(TestBase):
    def test_remove_loads(self):
        response = self.client.get('/remove', content_type='html/text')
        self.assertTrue(b'Update or Remove' in response.data)

    def test_add1(self):
        with self.client:
            response = self.client.post(
                    '/remove',
                    data=dict(
                        burnt=100,
                        intake=100,
                        calorie_id= 1
                    ),
                    follow_redirects=True
                    )
            self.assertIn(b'Update or Remove',response.data)
 

