from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from .twitch_locators import TwitchLocators

class TwitchPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_twitch(self):
        self.driver.get("https://www.twitch.tv/")
        sleep(3)

    def click_browse_icon(self):
        browse_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TwitchLocators.BUTTON_BROWSE)
        )
        browse_icon.click()

    def input_search(self, search_term):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TwitchLocators.SEARCH_INPUT)
        )
        search_input.send_keys(search_term + Keys.RETURN)

    def scroll_down(self, times):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 1000);")
            sleep(1)

    def select_streamer(self):
        streamer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TwitchLocators.STREAMER_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", streamer_link)
        self.driver.execute_script("arguments[0].click();", streamer_link)

    def wait_for_streamer_page_to_load(self):
        self.close_modal_if_present()
        streamer_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TwitchLocators.STREAMER_CONTENT_LOCATOR)
        )
        assert streamer_element is not None, "Streamer page not loaded, element was not found!"

    def close_modal_if_present(self):
        try:
            modal_close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TwitchLocators.MODAL_CLOSE_BUTTON)
            )
            modal_close_button.click()
            print("Modal closed.")
        except Exception as e:
            print("No modal found or could not close: ", str(e))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)