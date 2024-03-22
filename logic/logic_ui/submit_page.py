import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class PetStoreSubmitPage(BasePage):
    ROBOT_BUTTON = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="CustomerPassword"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.not_robot_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.ROBOT_BUTTON))
        self.submit_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))

    def not_robot_btn(self):
        self.not_robot_button.click()

    def submit_btn(self):
        self.submit_button.click()

