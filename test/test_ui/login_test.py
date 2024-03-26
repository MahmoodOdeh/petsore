import concurrent.futures
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.log_in_page import PetStoreLoginPage
from logic.logic_ui.submit_page import PetStoreSubmitPage


class PetStorePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_login(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.petstore.press_user_btn()
        self.login = PetStoreLoginPage(driver)
        self.login.user_name_fill("test.petstore@gmail.com")
        self.login.password_fill("pet12345678")
        time.sleep(5)
        self.login.sign_in_button.click()
        time.sleep(5)
        expected_title = "Account – Petstore.com"
        assert expected_title == driver.title, f"Expected title '{expected_title}', but got '{driver.title}'"

    def test_invalid_login(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.petstore.press_user_btn()
        self.login = PetStoreLoginPage(driver)
        self.login.user_name_fill("")
        self.login.password_fill("")
        self.login.sign_in_button.click()
        time.sleep(5)
        print(driver.title)
        expected_title = "Incorrect email or password. – Petstore.com"
        assert expected_title == driver.title, f"Expected title '{expected_title}', but got '{driver.title}'"

    def test_wrong_data_login(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.petstore.press_user_btn()
        self.login = PetStoreLoginPage(driver)
        self.login.user_name_fill("alexander@gmail.com")
        self.login.password_fill("12ii")
        self.login.sign_in_button.click()
        time.sleep(5)
        self.submit = PetStoreSubmitPage(driver)
       # self.submit.not_robot_btn()
        self.submit.submit_btn()
        time.sleep(3)
        print(driver.title)
        expected_title = "Incorrect email or password. – Petstore.com"
        assert expected_title == driver.title, f"Expected title '{expected_title}', but got '{driver.title}'"

    def test_run_grid_parallel_test_login(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_login, self.browser.browser_types)
        else:

            self.test_login(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_invalid_login(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_invalid_login, self.browser.browser_types)
        else:

            self.test_invalid_login(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_wrong_data_login(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_wrong_data_login, self.browser.browser_types)
        else:

            self.test_wrong_data_login(self.browser.default_browser.lower())
