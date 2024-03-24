import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.cart_page import PetStoreCartPage
from infra.cookie import cookies


class PetStorePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_cart_minus(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        for cookie_data in cookies:
            driver.add_cookie({
                'name': cookie_data['name'],
                'value': cookie_data['value'],
                'path': cookie_data.get('Path', '/'),
                'domain': cookie_data.get('Domain', ''),
            })
        driver.refresh()
        self.petstore = PetStorePage(driver)
        self.petstore.press_wagon_btn()
        self.quantity = PetStoreCartPage(driver)
        self.quantity.press_minus_btn()
        expected_title = "Petstore.com"
        assert expected_title == driver.title, f"Expected title '{expected_title}', but got '{driver.title}'"

    def test_cart_plus(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        for cookie_data in cookies:
            driver.add_cookie({
                'name': cookie_data['name'],
                'value': cookie_data['value'],
                'path': cookie_data.get('Path', '/'),
                'domain': cookie_data.get('Domain', ''),
            })
        driver.refresh()
        self.petstore = PetStorePage(driver)
        self.petstore.press_wagon_btn()
        self.quantity = PetStoreCartPage(driver)
        self.quantity.press_plus_btn()
        print(driver.title)
        expected_title = "Petstore.com"
        assert expected_title == driver.title, f"Expected title '{expected_title}', but got '{driver.title}'"


    def test_run_grid_parallel_test_cart_plus(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_cart_plus, self.browser.browser_types)
        else:
            self.test_cart_plus(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_cart_minus(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_cart_minus, self.browser.browser_types)
        else:
            self.test_cart_minus(self.browser.default_browser.lower())
