import time

from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class PetStorePage(BasePage):
    MENU_BUTTON = (By.XPATH, "//button[@class='site-nav__link site-nav__link--icon js-drawer-open-nav']")
    WAGON_BUTTON = (By.XPATH, "//a[@class='site-nav__link site-nav__link--icon js-drawer-open-cart js-no-transition']")
    USER_BUTTON = (
        By.XPATH, '//*[@id="shopify-section-header"]/div[3]/div[2]/div/div/header/div[1]/div/div[3]/div/div/a[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = self._driver.find_element(*self.MENU_BUTTON)
        self.wagon_button = self._driver.find_element(*self.WAGON_BUTTON)
        self.user_button = self._driver.find_element(*self.USER_BUTTON)

    def press_menu_btn(self):
        try:
            self.menu_button.click()
            time.sleep(2)
        except AttributeError:
            print("Menu button not found or is not clickable.")

    def press_wagon_btn(self):
        try:
            self.wagon_button.click()
            time.sleep(2)
        except AttributeError:
            print("Menu button not found or is not clickable.")

    def press_user_btn(self):
        try:
            self.user_button.click()
            time.sleep(2)
        except AttributeError:
            print("Menu button not found or is not clickable.")
