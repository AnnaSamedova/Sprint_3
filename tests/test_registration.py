from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helper import *

link_registration_form = "https://stellarburgers.nomoreparties.site/register"
link_page_login = "https://stellarburgers.nomoreparties.site/login"
email = get_fake_email()
password = get_fake_password()


class TestRegistration:

    def test_successful_registration_in_the_registration_form(self, browser):
        browser.get(link_registration_form)
        browser.find_element(*Locators.reg_name).send_keys(get_fake_name())
        browser.find_element(*Locators.reg_email).send_keys(email)
        browser.find_element(*Locators.reg_password).send_keys(password)
        browser.find_element(*Locators.reg_button).click()
        browser.get(link_page_login)
        browser.find_element(*Locators.auth_email).send_keys(email)
        browser.find_element(*Locators.auth_password).send_keys(password)
        browser.find_element(*Locators.auth_button).click()
        assert WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))

    def test_error_for_invalid_password_in_the_registration_form(self, browser):
        browser.get(link_registration_form)
        browser.find_element(*Locators.reg_name).send_keys(get_fake_name())
        browser.find_element(*Locators.reg_email).send_keys(get_fake_email())
        browser.find_element(*Locators.reg_password).send_keys('1')
        browser.find_element(*Locators.reg_button).click()
        assert WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.reg_error))
