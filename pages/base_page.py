import random
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.custom_webdriver import CustomWebDriver

class BasePage:

    def __init__(self, driver: CustomWebDriver) -> None:
        self.driver = driver

    def navigate_to_url(self, url: str):
        self.driver.get(url)
        self.driver.wait_for_url_match(url)
    
    def type_text(self, by, value, text: str):
        element = self.driver.find_element(by, value)
        element.send_keys(text)
    
    def get_texts(self, by, value) -> list:
        texts = [el.text for el in self.driver.find_elements(by, value)]
        return texts
    
    def get_attribute(self, by, value, attr_name):
        attr = self.driver.find_element(by, value).get_attribute(attr_name)
        logging.getLogger("DEBUG").info(f"====> attr: {attr}")
        return attr
    
    def check_attribute_is(self, by, value, attr_name, expected_attr_value):
        attr = self.driver.find_element(by, value).get_attribute(attr_name)
        logging.getLogger("DEBUG").info(f"====> attr: {attr}")
        if attr == expected_attr_value:
            return True
        else:
            return False

    def log(self, logger: str, level: str, content: str):
        logger_instance = logging.getLogger(logger)
        log_method = getattr(logger_instance, level.lower(), None)
        if log_method:
            log_method(content)
        else:
            raise Exception(f"Invalid log level: {level}. Please provide a valid one!")