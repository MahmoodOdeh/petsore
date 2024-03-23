import concurrent.futures
import time
import unittest

from selenium import webdriver

from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.menu_page import PetStoreMenuPage
from logic.logic_ui.cart_page import PetStoreCartPage
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
        self.petstore.press_menu_btn()
        self.menu = PetStoreMenuPage(driver)
        self.menu.press_dog_btn()

    def test_get_quantity(self, browser_type=None):
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
        self.cart = PetStoreCartPage(driver)
        quantity = self.cart.cart_quantity()
        print(quantity)
        self.assertEqual(quantity, "3", "Cart quantity update failed")

    def test_run_grid_parallel_test_get_quantity(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_get_quantity, self.browser.browser_types)
        else:

            self.test_get_quantity(self.browser.default_browser.lower())
