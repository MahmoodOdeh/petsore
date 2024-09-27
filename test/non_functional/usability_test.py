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

    def test_usability(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get(self.browser.get_driver_url())
        self.petstore = PetStorePage(driver)
        self.petstore.press_menu_btn()
        self.menu = PetStoreMenuPage(driver)
        self.menu.press_dog_btn()
        self.search = PetStoreSearchPage(driver)
        self.search.press_search_btn()
        self.search.search_fill("dog food")
        self.assertTrue(self.search.is_search_results_displayed(), "Search results not displayed")

    def test_run_grid_parallel_test_usability(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_usability, self.browser.browser_types)
        else:
            self.test_usability(self.browser.default_browser.lower())
