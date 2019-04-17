from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from django.test import TestCase
import re


class WebTestCase(TestCase):
    def setUp(self):
        pass

    def test_success_response(self):
        browser = webdriver.Remote(command_executor='http://selenium-chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

        print("Made it to test")
        browser.get("http://www.python.org")
        title = str(browser.title)
        print(title)
        browser.quit()

        self.assertIn('Python', title)

    def test_homepage(self):
        browser = webdriver.Remote(command_executor='http://selenium-chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

        browser.get("http://web:8000")
        title = browser.find_element_by_tag_name("h1").text
        browser.quit()

        self.assertIn('What is Sothebys?', title)

    def test_login(self):
        browser = webdriver.Remote(command_executor='http://selenium-chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

        browser.get('http://web:8000/login/')
        login = browser.find_element_by_name("email")
        pwd = browser.find_element_by_name("password")
        login.send_keys("roman.sharykin@gmail.com")
        pwd.send_keys("password")

        pwd.send_keys(Keys.RETURN)

        url = browser.current_url

        self.assertIn('http://web:8000', url)

    def tearDown(self):
        pass
