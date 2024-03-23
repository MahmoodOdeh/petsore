from selenium import webdriver
from infra.config_handler import ConfigHandler


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        config_file_path = 'C:/Users/odehm/Desktop/seleniumGrid/PetStore/config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.grid_enabled = self.config_handler.get_config_value('grid')
        self.serial_enabled = self.config_handler.get_config_value('serial')
        self.browser_types = self.config_handler.get_config_value('browser_types')
        self.default_browser = self.config_handler.get_config_value('browser')
        self.platform = self.config_handler.get_config_value('platform')
        self.hub_url = self.config_handler.get_config_value('hub_url')
        self.url = self.config_handler.get_config_value('url')

    def get_driver(self, browser_type=None):
        if browser_type:
            if browser_type.lower() == 'chrome':
                print("open chrome")
                return webdriver.Chrome()
            elif browser_type.lower() == 'edge':
                print("open edge")
                return webdriver.Edge()
            elif browser_type.lower() == 'firefox':
                print("open firefox")

                return webdriver.Firefox()
            else:
                return

        if self.grid_enabled and not self.serial_enabled:
            self.driver = self.get_grid_driver()
        else:
            self.driver = self.get_serial_driver()
        return self.driver

    def get_grid_driver(self):
        for browser_type in self.browser_types:
            if browser_type.lower() == 'chrome':
                print("open chrome")
                capabilities = webdriver.ChromeOptions()
            elif browser_type.lower() == 'edge':
                print("open edge")
                capabilities = webdriver.EdgeOptions()
            else:
                print("open firefox")
                capabilities = webdriver.FirefoxOptions()

            capabilities.capabilities['platformName'] = self.platform
            return webdriver.Remote(command_executor=self.hub_url, options=capabilities)

    def get_serial_driver(self):
        if self.default_browser.lower() == 'chrome':
            return webdriver.Chrome()
        elif self.default_browser.lower() == 'edge':
            return webdriver.Edge()
        else:
            return webdriver.Firefox()

    def driver_quit(self):
        if self.driver:
            self.driver.quit()
        else:
            print("no browser to close")

    def get_driver_url(self):
        return self.url
