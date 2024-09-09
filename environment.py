import logging
import json
import os
import platform
from pathlib import Path
from configparser import ConfigParser
from datetime import datetime
from behave.runner import Context
from behave import *
import allure
from allure import attach
from allure_commons.types import AttachmentType
from allure_behave.hooks import allure_report
from utils.driver_factory import DriverFactory

config = json.load(open("config.json"))

@fixture
def pre_test_execution(context):
    config_parser = ConfigParser()
    config_parser.read("behave.ini")
    context.report_dirname = os.path.join(os.getcwd(), os.path.normpath(f"reports/{datetime.now().strftime('%d%m%Y_%H%M%S')}"))
    config_parser['behave']['outfiles'] = context.report_dirname
    with open("behave.ini", "w") as configfile:
        config_parser.write(configfile)
    logging.getLogger("behave").info(f"Behave tests output saved in: {config_parser['behave']['outfiles']}")

@fixture
def setup_driver(context: Context):
    env = config.get("env", "stage")
    if not os.path.exists(os.path.normpath(f"data/{env}.json")):
        raise Exception(f"Plese provide correct env, environment: {env} is not support yet")
    logging.getLogger("behave").info(f"Using environment: {env}")
    context.env_data = json.load(open(os.path.normpath(f"data/{env}.json"), encoding="UTF-8"))
    context.driver = DriverFactory(config, context).driver()
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(setup_driver, context)

def before_feature(context, feature):
    context.feature = feature
    logging.getLogger("behave").info(f">>>>>>>>>> FEATURE: {context.feature.name} <<<<<<<<<<")

def before_scenario(context, scenario):
    context.scenario = scenario
    logging.getLogger("behave").info(f"---------- SCENARIO: {context.scenario.name} ----------")

def before_step(context, step):
    context.step = step

def after_step(context,step):
    attach_screenshot(context)
    logging.getLogger("behave").info(f"{context.step.name} - {context.step.status}")


def attach_screenshot(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def write_environment_properties(context):
    environment_info = {
        "OS": platform.platform(),
        "OS_Version": platform.version(),
        "Python_Version": platform.python_version(),
        "Browser": context.driver.capabilities["browserName"],
        "Browser_Version": context.driver.capabilities["browserVersion"],
        "URL": context.env_data.get("url")
    }
    logging.getLogger("behave").info(f"environment information: {environment_info} \n")
    environment_path = os.path.normpath(f"{os.getcwd()}/reports/temp/environment.properties")
    with open(environment_path, "w") as file:
        for key, value in environment_info.items():
            file.write(f"{key}={value}\n")

def after_all(context):
    write_environment_properties(context)
    os.rename(os.path.normpath(f"{os.getcwd()}/reports/temp"), os.path.normpath(f"{os.getcwd()}/reports/{datetime.now().strftime('%d%m%Y_%H%M%S')}"))