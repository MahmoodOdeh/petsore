import time
import unittest
from http import cookies as http_cookies

from selenium import webdriver

from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.log_in_page import PetStoreLoginPage
from logic.logic_ui.submit_page import PetStoreSubmitPage
from logic.logic_ui.menu_page import PetStoreMenuPage
from infra.cookie import cookies


class PetStorePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_press_menu(self):
        driver = self.browser.get_driver()
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.petstore.press_user_btn()
        self.login = PetStoreLoginPage(driver)
        self.login.user_name_fill("test.petstore@gmail.com")
        self.login.password_fill("pet12345678")
        self.login.sign_in_button.click()
        self.submit = PetStoreSubmitPage(driver)
        self.submit.not_robot_button()
        self.submit.submit_button()

