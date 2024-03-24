from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from infra.base_page import BasePage


class PetStoreMenuPage(BasePage):
    DOG_CATEGORY = (By.XPATH,
                    '//*[@id="Label-collections-dog1"] ')

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.dog_category = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.DOG_CATEGORY))

    def press_dog_btn(self):
        self.dog_category.click()
