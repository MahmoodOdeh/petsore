import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.home_page import PetStorePage
from logic.logic_ui.menu_page import PetStoreMenuPage
from logic.logic_ui.search_page import PetStoreSearchPage


class PetStorePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.driver_quit()

    def test_search(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.search = PetStoreSearchPage(driver)
        self.search.press_search_btn()
        self.search.search_fill("cat food")
        self.search.press_search_left_btn()
        print(driver.title)
        expected = 'Search: 257 results found for "cat food*" – Petstore.com'
        self.assertEqual(expected, driver.title, "Page title does not match expected title")

    def test_wrong_search(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.search = PetStoreSearchPage(driver)
        self.search.press_search_btn()
        self.search.search_fill("adidas")
        self.search.press_search_left_btn()
        print(driver.title)
        expected = 'Search: 0 results found for "adidas*" – Petstore.com'
        self.assertEqual(expected, driver.title, "Page title does not match expected title")

    def test_empty_search(self, browser_type=None):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.search = PetStoreSearchPage(driver)
        self.search.press_search_btn()
        self.search.search_fill("")
        self.search.press_search_left_btn()
        print(driver.title)
        expected = 'Search – Petstore.com'
        self.assertEqual(expected, driver.title, "Page title does not match expected title")

    def test_run_grid_parallel_test_search(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search, self.browser.browser_types)
        else:
            self.test_search(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_wrong_search(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_wrong_search, self.browser.browser_types)
        else:
            self.test_wrong_search(self.browser.default_browser.lower())

    def test_run_grid_parallel_test_empty_search(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_empty_search, self.browser.browser_types)
        else:
            self.test_empty_search(self.browser.default_browser.lower())
