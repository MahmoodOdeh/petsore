import time

from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class PetStoreCartPage(BasePage):
    QUANTITY = (By.XPATH, '//*[@id="updates_32809880223819:9f641301f24bb2a7bdf14d6c8242474e"]')
    MINUS = (By.XPATH, '//button[@aria-label="Reduce item quantity by one"]')
    PLUS = (By.XPATH, '//button[@aria-label="Increase item quantity by one"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.quantity = self._driver.find_element(*self.QUANTITY)
        self.plus = self._driver.find_element(*self.PLUS)
        self.minus = self._driver.find_element(*self.MINUS)

    def cart_quantity(self):
        quantity_value = self.quantity.get_attribute('value')
        return quantity_value

    def press_plus_btn(self):
        try:
            self.plus.click()
            time.sleep(2)
        except AttributeError:
            print("plus button not found or is not clickable.")

    def press_minus_btn(self):
        try:
            self.minus.click()
            time.sleep(2)
        except AttributeError:
            print("minus button not found or is not clickable.")

    def press_minus_plus_flow(self):
        self.press_plus_btn()
        time.sleep(2)
        self.press_minus_btn()
