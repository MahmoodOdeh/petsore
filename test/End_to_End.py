import concurrent.futures
import unittest
from ..infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from infra.headers import headers
from infra.payload import payload
from logic.logic_api.petstore_Api import PetStore
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.cart_page import PetStoreCartPage
from infra.cookie import cookies


class PetStorePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_get_quantity(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.my_api = APIWrapper()
        self.api_cart = PetStore(self.my_api, self.browser.url)
        self.response = self.api_cart.Add_Cart_api_json(headers=headers, payload=payload)
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
        print(self.response['quantity'])
        self.assertEqual(int(quantity), self.response['quantity'], "Cart quantity update failed")

    def test_run_grid_parallel_test_get_quantity(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_get_quantity, self.browser.browser_types)
        else:
            self.test_get_quantity(self.browser.default_browser.lower())
