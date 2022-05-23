from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import JSONManager


def get_page_content(page: str):
    browser.get(page)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    return soup.prettify()


def initialize_firefox(gecko_path: str):
    mozilla_service = Service(gecko_path)
    firefox_options = FirefoxOptions()
    #firefox_options.add_argument("--headless")
    browser = webdriver.Firefox(service=mozilla_service, options=firefox_options )
    browser.set_window_size(1366, 786)
    return browser


def login_to_hss_is(browser, username: str, password: str, success_page: str = None):
    browser.get("https:/hss-is.com")
    browser.find_element(By.ID, "tijelo_txtLozinka").send_keys(password)
    browser.find_element(By.ID, "tijelo_txtUser").send_keys(username)
    browser.find_element(By.ID, "tijelo_btnPrijava").click()
    if success_page is not None:
        if browser.current_url == success_page:
            return True
        return False
    return True


settings = JSONManager.load_json("Settings.json")
gecko_path = settings["Firefox"]["gecko_path"]
username = settings["Login"]["account"]
password = settings["Login"]["password"]

browser = initialize_firefox(gecko_path)
login_to_hss_is(browser, username, password)
