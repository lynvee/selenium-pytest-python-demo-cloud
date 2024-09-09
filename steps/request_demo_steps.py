from behave import *
import logging
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.docs_page import DocsPage
from pages.register_demo_page import RegisterDemoPage

@when("Click on `Request a demo` button")
def click_request_demo(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_to_register_demo_page()

@then("Verify if navigating to correct Register Demo page")
def verify_register_page(context):
    context.register_demo_page = RegisterDemoPage(context.driver)
    context.current_url = context.register_demo_page.get_register_demo_page_url()
    context.register_demo_page.verify_register_demo_page_url(context.current_url, context.env_data["register_demo"]["register_demo_page_url"])
    context.current_title = context.register_demo_page.get_current_title()
    context.register_demo_page.verify_register_demo_page_title(context.current_title, context.env_data["register_demo"]["title"])

@when("Enter {data} information to the form")
def enter_valid_data(context):
    context.register_demo_page = RegisterDemoPage(context.driver)

@when("Test")
def test(context):
    context.register_demo_page = RegisterDemoPage(context.driver)
    context.register_demo_page.enter_data_request_form()
