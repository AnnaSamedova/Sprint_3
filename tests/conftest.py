import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import Locators

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"


@pytest.fixture()
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1900,1100')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    browser.get(link_stellar_burgers)
    browser.find_element(*Locators.button_auth_home_page).click()
    browser.find_element(*Locators.auth_email).send_keys('anna@yandex.ru')
    browser.find_element(*Locators.auth_password).send_keys('123456')
    browser.find_element(*Locators.auth_button).click()
    return browser
