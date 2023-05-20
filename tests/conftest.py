import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from locators import Locators
from faker import Faker

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"


@pytest.fixture(scope='function')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1900,1100')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login(browser):
    browser.get(link_stellar_burgers)
    browser.find_element(By.XPATH, Locators.button_auth_home_page).click()
    browser.find_element(By.NAME, Locators.auth_email).send_keys('anna@yandex.ru')
    browser.find_element(By.NAME, Locators.auth_password).send_keys('123456')
    browser.find_element(By.XPATH, Locators.auth_button).click()
    return browser


# Дополнительное задание


@pytest.fixture(scope='function')
def faker():
    return Faker()


@pytest.fixture(scope='function')
def fake_email(faker):
    return faker.email()


@pytest.fixture(scope='function')
def fake_name(faker):
    return faker.name()


@pytest.fixture(scope='function')
def fake_password(faker):
    return faker.password(6, 10)

