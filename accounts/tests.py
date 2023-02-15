from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from django.test import TestCase

# Create your tests here.

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_signup(self):
        # visit signup url
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/register/'))

        # fill sign up form
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys("test@example.com")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('testuser')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.send_keys('password@1')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.send_keys('password@1')

        # submit signup form
        submit_btn = self.selenium.find_element(By.XPATH, '//button[text()="Register"]')
        self.selenium.execute_script("arguments[0].click();", submit_btn)
        
        try:
            # wait till server responses with success message; 10 sec timeout
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.messages'))
            WebDriverWait(self.selenium, timeout=10).until(element_present) # 10 sec timeout

            # assert success message in response
            msg_success = self.selenium.find_element(By.CSS_SELECTOR, 'li.success').text()
            self.assertEquals(msg_success, "Registration successful!! Please activate your email")

        except TimeoutException as exc:
            raise exc
