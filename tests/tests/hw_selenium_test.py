from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv
from unittest import TestCase


load_dotenv()

class TestAuthorization(TestCase):
    def test_ya_authorization(self):
        driver = webdriver.Chrome()

        driver.get('https://passport.yandex.ru/auth/')
        time.sleep(3)
        login = driver.find_element(By.ID, 'passp-field-login')
        login.send_keys(os.getenv('YA_LOGIN'))
        login.send_keys(Keys.ENTER)
        time.sleep(3)

        password = driver.find_element(By.ID, 'passp-field-passwd')
        password.send_keys(os.getenv('YA_PASSWORD'))
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        driver.close()
        driver.quit()
