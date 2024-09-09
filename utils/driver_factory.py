import logging
from behave.runner import Context
from datetime import datetime
from selenium import webdriver
from utils.custom_webdriver import CustomWebDriver
from utils.event_listener import EventListener

class DriverFactory:

    log_filename = datetime.now().strftime("%d%m%Y") + ".log"
    logging.basicConfig(filename=log_filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(name)-10s - %(levelname)-10s - %(message)s',
                        datefmt="%H:%M:%S",
                        encoding="UTF-8")
    
    def __init__(self, config, context: Context):
        self.config = config
        self.context = context
        self.logger = logging.getLogger("selenium")
    
    def driver(self):
        if self.config["browser"]=="chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument('--no-sandbox')
            # .add_argument("--disable-dev-shm-usage")
            if self.config["headless-mode"]:
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
            _driver = CustomWebDriver(
                driver=webdriver.Chrome(options=options),
                event_listener=EventListener(logger=self.logger, time_out=self.config["explicit"]),
                config=self.config,
                logger=self.logger
            )
        else:
            raise Exception("Please provide valid browser name!")
        return _driver