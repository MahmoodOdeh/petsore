import concurrent.futures
import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.petstore_Api import PetStore
from infra.headers import headers
from infra.payload import payload


class TestCart(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_cart = PetStore(self.my_api, self.browser.url)
        self.response = self.api_cart.Add_Cart_api_json(headers=headers, payload=payload)

    def tearDown(self):
        self.browser.driver_quit()

    def test_add_product(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        print(self.response)
        self.assertEqual(self.response['id'], 32809880223819)
        self.assertEqual(self.response['properties'], {})
        self.assertEqual(self.response['variant_id'], 32809880223819)
        self.assertEqual(self.response['key'], '32809880223819:9f641301f24bb2a7bdf14d6c8242474e')
        self.assertEqual(self.response['title'], 'Jolly Pets® Push-n-Play™ Dog Toys Blue Color X-Large 14 Inch')
        self.assertEqual(self.response['price'], '64.97')
        self.assertEqual(self.response['original_price'], '64.97')
        self.assertEqual(self.response['presentment_price'], 64.97)
        self.assertEqual(self.response['total_discount'], '0.00')
        self.assertEqual(self.response['discounts'], [])
        self.assertEqual(self.response['sku'], '9031423')
        self.assertEqual(self.response['grams'], 2268)
        self.assertEqual(self.response['vendor'], 'Petstore')
        self.assertFalse(self.response['taxable'])
        self.assertEqual(self.response['product_id'], 4661007810635)
        self.assertTrue(self.response['product_has_only_default_variant'])
        self.assertFalse(self.response['gift_card'])

    def test_run_grid_parallel_test_add_product(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_add_product, self.browser.browser_types)
        else:
            self.test_add_product(self.browser.default_browser.lower())

