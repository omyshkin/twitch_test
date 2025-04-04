import pytest
from utils.webdriver_manager import WebDriverManager
from page_objects.twitch_page import TwitchPage

@pytest.fixture(scope="module")
def driver():
    driver = WebDriverManager.get_driver()
    yield driver
    driver.quit()

def test_twitch_streamer_search(driver):
    twitch_page = TwitchPage(driver)
    twitch_page.go_to_twitch()
    twitch_page.click_browse_icon()
    twitch_page.input_search("StarCraft II")
    twitch_page.scroll_down(2)
    twitch_page.select_streamer()
    twitch_page.wait_for_streamer_page_to_load()
    twitch_page.take_screenshot("streamer_page.png")