import concurrent.futures
import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.search_page import PetStoreSearchPage
from logic.logic_ui.home_page import PetStorePage


class PerformanceTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_assert_response_time_load_website(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        start_time = time.time()
        time.sleep(1)
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Page loaded in: {response_time:.2f} seconds")
        assert response_time < 5, "Page load time exceeded 5 seconds"

    def test_assert_response_time_search(self,browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.search = PetStoreSearchPage(driver)
        self.search.press_search_btn()
        self.search.search_fill("dog food")
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Search operation completed in: {response_time:.2f} seconds")
        assert response_time < 5, "Search operation took more than 5 seconds"
