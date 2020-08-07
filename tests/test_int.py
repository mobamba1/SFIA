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

test_burnt = 800
test_intake = 800
test_owner_id =86


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
        self.driver.get("http://34.72.106.127:5000/")

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")
        
    def test_server_is_up_and_running(self):
        response = urlopen("http://34.72.106.127:5000")
        self.assertEqual(response.code, 200)
        
class TestView(TestBase):
    def test_add(self):
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        time.sleep(1)
        assert url_for('add') in self.driver.current_url


    def test_adding(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="burnt"]').send_keys(test_burnt)
        self.driver.find_element_by_xpath('//*[@id="intake"]').send_keys(test_intake)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url

    def test_update(self):
        self.driver.find_element_by_xpath('/html/body/div/a[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="burnt"]').send_keys(test_burnt)
        self.driver.find_element_by_xpath('//*[@id="intake"]').send_keys(test_intake)
        self.driver.find_element_by_xpath('//*[@id="calorie_id"]').send_keys(test_owner_id)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        assert url_for('remove') in self.driver.current_url

#    def test_delete(self):
 #       self.driver.find_element_by_xpath('/html/body/div/a[3]').click()
  #      time.sleep(1)
   #     self.driver.find_element_by_xpath('/html/body/form/button').click()
    #    time.sleep(1)
     #   assert url_for('remove') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
