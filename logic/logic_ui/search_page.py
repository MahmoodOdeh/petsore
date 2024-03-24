import time
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class PetStoreSearchPage(BasePage):
    SEARCH_BUTTON = (
        By.XPATH, "//a[@class='site-nav__link site-nav__link--icon js-search-header js-no-transition']")
    SEARCH_FIELD = (By.XPATH, '//*[@id="HeaderSearchForm"]/input[2]')
    SEARCH_BUTTON_LEFT = (By.XPATH, '//*[@id="HeaderSearchForm"]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.search_button = self._driver.find_element(*self.SEARCH_BUTTON)
        self.search_field = self._driver.find_element(*self.SEARCH_FIELD)
        self.search_button_left = self._driver.find_element(*self.SEARCH_BUTTON_LEFT)

    def press_search_btn(self):
        try:
            self.search_button.click()
            time.sleep(2)
        except AttributeError:
            print("search button not found or is not clickable.")

    def search_fill(self, text):
        self.search_field.send_keys(text)
        time.sleep(5)

    def is_search_results_displayed(self):
        return bool(self._driver.find_element(By.XPATH, '//*[@id="HeaderSearchForm"]/input[2]'))

    def press_search_left_btn(self):
        try:
            self.search_button_left.click()
            time.sleep(2)
        except AttributeError:
            print("search button not found or is not clickable.")
