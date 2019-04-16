import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):
    """docstring forLoginTest."""
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:8000/login/")
        email = driver.find_element_by_name("email")
        email.send_keys("roman.sharykin@gmial.com")
        pwd = driver.find_element_by_name("password")
        pwd.send_keys("password")
        pwd.send_keys(Keys.RETURN)
        assert driver.current_url == "http://localhost:8000/login/"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
