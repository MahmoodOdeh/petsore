import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.petstore_Api import PetStore
from infra.headers import headers
from infra.payload import payload


class TestCartLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_cart = PetStore(self.my_api, self.browser.url)

    def test_add_product(self):
        print(self.api_cart.Add_Cart_api_json(headers=headers, payload=payload))


if __name__ == '__main__':
    unittest.main()
