import logging
import time
from selenium.webdriver.common.by import By
from utils.custom_webdriver import CustomWebDriver
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from pages.docs_page import DocsPage
from pages.register_demo_page import RegisterDemoPage

class HomePage(BasePage):

    def __init__(self, driver: CustomWebDriver) -> None:
        super().__init__(driver)
    
    # LOCATORS:
    MENU_TABS = (By.XPATH, "//tab[@jsaction]/a[@class='nKZVnd']")
    NEWS_TABS = (By.XPATH, "//span[contains(@id, 'ucj-1-')]")
    NEWS_TABS_TEXT = (By.XPATH, "//h4[contains(@id, 'ucj-1-')]")
    NEWS_TABS_TITTLE = {
        "What's new in AI": (By.XPATH, "//span[@id='ucj-1-0-tab']"),
        "Developers": (By.XPATH, "//span[@id='ucj-1-1-tab']"),
        "Business leaders": (By.XPATH, "//span[@id='ucj-1-2-tab']")
    }
    NEWS_TABS_TOPICS = {
        "What's new in AI": (By.XPATH,"//div[@id='ucj-1-0-panel']//p[@class='yTPOpb']"),
        "Developers": (By.XPATH, "//div[@id='ucj-1-1-panel']//p[@class='yTPOpb']"),
        "Business leaders": (By.XPATH, "//div[@id='ucj-1-2-panel']//p[@class='yTPOpb']")
    }
    NEWS_TABS_SUMMARY = {
        "What's new in AI": (By.XPATH, "//div[@id='ucj-1-0-panel']//p[not(@class)]"),
        "Developers": (By.XPATH, "//div[@id='ucj-1-1-panel']//p[not(@class)]"),
        "Business leaders": (By.XPATH, "//div[@id='ucj-1-2-panel']//p[not(@class)]")
    }
    DOCS_HEADER = (By.XPATH, "//a[text()='Docs']//parent::tab[@class='uHusBf']")
    REQUEST_DEMO_BUTTON = (By.XPATH, "//*[text()='Request a demo']")

    # ACTIONS:
    def get_menu_tabs(self):
        return self.get_texts(*self.MENU_TABS)
    
    def get_news_tabs(self):
        return self.get_texts(*self.NEWS_TABS_TEXT)

    def select_module_option(self, module: GetAttrFromDict):
        option_locator = (By.XPATH, f"//h5[contains(text(), '{module.title}')]")
        self.driver.click_element(*option_locator)
        self.driver.wait_for_url_match(module.expected_url)
    
    def get_current_news(self):
        news_tabs = self.get_news_tabs()
        select_tab = [tab.get_attribute("track-name") for tab in self.driver.find_elements(*self.NEWS_TABS) if self.check_attribute_is(*self.NEWS_TABS, "aria-selected", "true")][0]
        logging.getLogger("DEBUG").info(f"====> select_tab: {select_tab}")
        for key, _ in self.NEWS_TABS_TOPICS.items():
            if key.lower() == select_tab.lower():
                topics = self.get_texts(*self.NEWS_TABS_TOPICS[key])
                contents = self.get_texts(*self.NEWS_TABS_SUMMARY[key])
                ads_contents = self.process_ads_contents(topics, contents)
                break
        for tab in news_tabs:
            if select_tab.lower() == tab.lower():
                news_tabs.remove(tab)
        logging.getLogger("DEBUG").info(f"====> news_tabs after delete: {news_tabs}")
        return ads_contents, news_tabs
    
    def process_ads_contents(self, topics: list, contents: list):
        if len(topics)==len(contents):
            ads_contents = {}
            for i in range(len(topics)):
                ads_contents[topics[i]] = contents[i]
            logging.getLogger("DEBUG").info(f"====> ads_contents: {ads_contents}")
            return ads_contents

    def navigate_to_docs_page(self):
        self.driver.click_element(*self.DOCS_HEADER)
        return DocsPage(self.driver).wait_for_docs_page_loads()
        
    def navigate_to_register_demo_page(self):
        self.driver.click_element(*self.REQUEST_DEMO_BUTTON)
        return RegisterDemoPage(self.driver).wait_for_register_demo_page_loads()

    # VERIFICATION:
    def verify_menu_tabs_number(self, expected_menu_tabs):
        current_menu_tabs = self.get_menu_tabs()
        logging.getLogger("DEBUG").info(f"====> current_menu_tabs: {current_menu_tabs}")
        assert len(current_menu_tabs) == len(expected_menu_tabs)

    def verify_menu_tabs_info(self, expected_menu_tabs):
        current_menu_tabs = self.get_menu_tabs()
        logging.getLogger("DEBUG").info(f"====> current_menu_tabs: {current_menu_tabs}")
        assert current_menu_tabs == expected_menu_tabs

    def verify_news_tabs_number(self, expected_menu_tabs):
        current_news_tabs = self.get_news_tabs()
        logging.getLogger("DEBUG").info(f"====> current_news_tabs: {current_news_tabs}")
        assert len(current_news_tabs) == len(expected_menu_tabs)

    def verify_news_tabs_info(self, expected_menu_tabs):
        current_news_tabs = self.get_news_tabs()
        logging.getLogger("DEBUG").info(f"====> current_news_tabs: {current_news_tabs}")
        assert current_news_tabs == expected_menu_tabs

    def compare_ads_with_diff_tabs(self, current_ads: dict, remain_news_tabs: list):
        for tab in remain_news_tabs:
            for key, _ in self.NEWS_TABS_TITTLE.items():
                if tab.lower() == key.lower():
                    self.driver.click_element(*self.NEWS_TABS_TITTLE[key])
                    topics = self.get_texts(*self.NEWS_TABS_TOPICS[key])
                    contents = self.get_texts(*self.NEWS_TABS_SUMMARY[key])
                    ads_contents = self.process_ads_contents(topics, contents)
                    if current_ads == ads_contents:
                        return False