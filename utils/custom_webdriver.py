import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.common import ElementClickInterceptedException

class CustomWebDriver(EventFiringWebDriver):
    def __init__(self, driver: WebDriver, event_listener: AbstractEventListener, config, logger) -> None:
        super().__init__(driver, event_listener)
        self.driver = driver
        self.config = config
        self.logger = logger
        self.time_out = config["explicit"]
    
    def wait_for_url_match(self, url: str):
        wait = WebDriverWait(self.wrapped_driver, self.time_out)
        wait.until(EC.url_to_be(url))

    def wait_for_presence_of_elements(self, by, value):
        wait = WebDriverWait(self.wrapped_driver, self.time_out)
        wait.until(EC.presence_of_all_elements_located((by, value)))

    def wait(self, seconds: int=5):
        time.sleep(seconds)
    
    def scroll_to_element(self, by, value):
        element = self.find_element(by, value)
        element.location_once_scrolled_into_view
    
    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.location_once_scrolled_into_view
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
