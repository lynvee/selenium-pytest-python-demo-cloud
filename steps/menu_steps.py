from behave import *
import logging
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.docs_page import DocsPage
from pages.register_demo_page import RegisterDemoPage

@given("Go to Demo page")
def navigate_to_demo(context):
    context.base_page = BasePage(context.driver)
    context.base_page.navigate_to_url(context.env_data["url"])

@then("Verify number of menu tabs")
def verify_number_tabs(context):
    context.home_page = HomePage(context.driver)
    expected_menu_tabs = context.env_data["menu"]["menu_tabs"]
    logging.getLogger("DEBUG").info(f"====> expected_menu_tabs: {expected_menu_tabs}")
    context.home_page.verify_menu_tabs_number(expected_menu_tabs)

@then("Verify information of menu tabs")
def verify_tabs_infor(context):
    context.home_page = HomePage(context.driver)
    expected_menu_tabs = context.env_data["menu"]["menu_tabs"]
    logging.getLogger("DEBUG").info(f"====> expected_menu_tabs: {expected_menu_tabs}")
    context.home_page.verify_menu_tabs_info(expected_menu_tabs)

@then("Verify number of news tabs")
def verify_number_tabs(context):
    context.home_page = HomePage(context.driver)
    expected_news_tabs = context.env_data["news"]["news_tabs"]
    logging.getLogger("DEBUG").info(f"====> expected_news_tabs: {expected_news_tabs}")
    context.home_page.verify_news_tabs_number(expected_news_tabs)

@then("Verify information of news tabs")
def verify_tabs_infor(context):
    context.home_page = HomePage(context.driver)
    expected_news_tabs = context.env_data["news"]["news_tabs"]
    logging.getLogger("DEBUG").info(f"====> expected_news_tabs: {expected_news_tabs}")
    context.home_page.verify_news_tabs_info(expected_news_tabs)

@when("View news in current News Tab")
def view_news(context):
    context.home_page = HomePage(context.driver)
    context.current_news, context.remain_news_tabs = context.home_page.get_current_news()

@then("Compare news in current Tab with different News Tabs")
def compare_news(context):
    context.home_page = HomePage(context.driver)
    context.home_page.compare_ads_with_diff_tabs(context.current_news, context.remain_news_tabs)

@when("Click on `Docs` header")
def click_docs_header(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_to_docs_page()

@then("Verify if navigating to correct Documentation page")
def verify_docs_page(context):
    context.docs_page = DocsPage(context.driver)
    context.current_url = context.docs_page.get_docs_page_url()
    context.docs_page.verify_docs_page_url(context.current_url, context.env_data["docs"]["docs_page_url"])
    context.current_title = context.docs_page.get_current_title()
    context.docs_page.verify_docs_page_title(context.current_title, context.env_data["docs"]["title"])
