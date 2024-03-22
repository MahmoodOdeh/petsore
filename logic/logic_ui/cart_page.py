import time

from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class PetStoreCartPage(BasePage):
    QUANTITY = (By.ID, 'updates_32809880223819:9f641301f24bb2a7bdf14d6c8242474e')

    def __init__(self, driver):
        super().__init__(driver)
        self.quantity = self._driver.find_element(*self.QUANTITY)

    def cart_quantity(self):
        quantity_value = self.quantity.get_attribute('value')
        return quantity_value
