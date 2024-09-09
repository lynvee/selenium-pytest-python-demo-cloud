import logging
import time
from selenium.webdriver.common.by import By
from utils.custom_webdriver import CustomWebDriver
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage

class RegisterDemoPage(BasePage):

    def __init__(self, driver: CustomWebDriver) -> None:
        super().__init__(driver)
    
    # LOCATORS:
    REGISTOR_DEMO_PAGE_TITLE = (By.XPATH, "//h3[@id='talk-to-a-google-cloud-sales-specialist']")
    
    # ACTIONS:
    def wait_for_register_demo_page_loads(self):
        self.driver.wait_for_presence_of_elements(*self.REGISTOR_DEMO_PAGE_TITLE)

    def get_current_title(self):
        return self.driver.find_element(*self.REGISTOR_DEMO_PAGE_TITLE).text.strip()

    def get_register_demo_page_url(self):
        return self.driver.current_url

    def enter_data_request_form(self):
        first_name_shadow_host = (By.XPATH, "//cws-textfield[@name='FirstName']")
        first_name_location = (By.CSS_SELECTOR, "[@name='FirstName']")
        first_name_shadow_root = self.driver.find_element(*first_name_shadow_host).shadow_root
        logging.getLogger("DEBUG").info(f"====> first_name_shadow_root: {first_name_shadow_root}")

    # VERIFICATION:
    def verify_register_demo_page_url(self, current_url, expected_url):
        assert current_url == expected_url

    def verify_register_demo_page_title(self, current_register_title, expected_register_title):
        assert current_register_title==expected_register_title
