from .config import *

def load_url():
    #load url in browser
    browser.driver.get("https://kitabisa.com")
    landing_page = browser.driver.find_element_by_id("home-page")
    browser.driver.implicitly_wait(10)
    assert landing_page