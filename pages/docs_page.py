import logging
import time
from selenium.webdriver.common.by import By
from utils.custom_webdriver import CustomWebDriver
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage

class DocsPage(BasePage):

    def __init__(self, driver: CustomWebDriver) -> None:
        super().__init__(driver)
    
    # LOCATORS:
    DOCS_PAGE_TITLE = (By.XPATH, "//h3[@id='google-cloud-documentation']")

    # ACTIONS:
    def wait_for_docs_page_loads(self):
        self.driver.wait_for_presence_of_elements(*self.DOCS_PAGE_TITLE)
    
    def get_current_title(self):
        return self.driver.find_element(*self.DOCS_PAGE_TITLE).text.strip()

    def get_docs_page_url(self):
        return self.driver.current_url

    # VERIFICATION:
    def verify_docs_page_url(self, current_url, expected_url):
        assert current_url == expected_url

    def verify_docs_page_title(self, current_docs_title, expected_docs_title):
        assert current_docs_title==expected_docs_title