import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class PetStoreLoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, '//*[@id="CustomerEmail"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="CustomerPassword"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="customer_login"]/p[1]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.email_field = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.EMAIL_FIELD))
        self.password_field = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        self.sign_in_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))

    def user_name_fill(self, text):
        actions = ActionChains(self._driver)
        actions.click(self.email_field).perform()
        self.email_field.send_keys(text)

    def password_fill(self, text):
        actions = ActionChains(self._driver)
        actions.click(self.password_field).perform()
        self.password_field.send_keys(text)

    def sign_in_button(self):
        self.sign_in_button.click()
