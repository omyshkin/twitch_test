from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class WebDriverManager:
    @staticmethod
    def get_driver():
        mobile_emulation = {
            "deviceName": "Samsung Galaxy S8+"
        }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        try:
            driver = webdriver.Chrome(options=options)
            return driver
        except WebDriverException as e:
            print(f"Failed to initialize WebDriver: {str(e)}")
            raise