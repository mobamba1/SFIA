import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Adding

test_burnt = 300
test_intake = 300
test_ownder_id =10


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/kenneth1521412/SFIA/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://35.238.140.108:5000")

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://35.238.140.108:5000")
        self.assertEqual(response.code, 200)


class TestView(TestBase):
    def test_add(self):
        self.driver.find_element_by_xpath('<a href="/add">Add Calories</a>').click()
        time.sleep(1)
        assert url_for('add') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
