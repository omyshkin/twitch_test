from selenium.webdriver.common.by import By

class TwitchLocators:
    BUTTON_BROWSE = (By.XPATH, "//div[text()='Browse']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    STREAMER_LINK = (By.XPATH, "//button[contains(@class, 'tw-link')]//p[text()='StarCraft II']")
    STREAMER_CONTENT_LOCATOR  =  (By.CSS_SELECTOR,  "div[data-a-target='video-player'] div[data-a-target='player-controls']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='content-classification-gate-overlay-start-watching-button']")