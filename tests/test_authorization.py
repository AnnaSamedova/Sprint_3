from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"
link_registration_form = "https://stellarburgers.nomoreparties.site/register"
link_forgot_password = "https://stellarburgers.nomoreparties.site/forgot-password"


class TestAuthorization:

    def test_authorization_with_the_button_login_to_account(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(*Locators.button_auth_home_page).click()
        browser.find_element(*Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(*Locators.auth_password).send_keys('123456')
        browser.find_element(*Locators.auth_button).click()
        assert WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))

    def test_authorization_with_the_button_personal_account(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(*Locators.button_account).click()
        browser.find_element(*Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(*Locators.auth_password).send_keys('123456')
        browser.find_element(*Locators.auth_button).click()
        assert WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))

    def test_authorization_in_the_registration_form(self, browser):
        browser.get(link_registration_form)
        browser.find_element(*Locators.button_auth_reg_page).click()
        browser.find_element(*Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(*Locators.auth_password).send_keys('123456')
        browser.find_element(*Locators.auth_button).click()
        assert WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))

    def test_authorization_in_the_password_recovery_form(self, browser):
        browser.get(link_forgot_password)
        browser.find_element(*Locators.button_auth_reg_page).click()
        browser.find_element(*Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(*Locators.auth_password).send_keys('123456')
        browser.find_element(*Locators.auth_button).click()
        assert WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))
