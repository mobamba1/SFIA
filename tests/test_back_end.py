import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Adding, User
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLACHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
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
        response = self.client.get(url_for('remove'))
        self.assertEqual(response.status_code, 200)

 

