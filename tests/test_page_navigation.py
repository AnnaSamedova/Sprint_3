from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestPageNavigation:

    def test_go_to_personal_account_with_click_on_personal_account_in_the_header(self, login):
        login.find_element(*Locators.button_account).click()
        assert WebDriverWait(login, 10).until(
            EC.presence_of_element_located(Locators.text_personal_data)).text

    def test_go_to_constructor_from_personal_account_with_click_on_logo(self, login):
        login.find_element(*Locators.button_account).click()
        login.find_element(*Locators.logo).click()
        assert WebDriverWait(login, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))

    def test_go_to_constructor_from_personal_account_by_click_on_constructor_in_the_header(self, login):
        login.find_element(*Locators.button_account).click()
        login.find_element(*Locators.constructor).click()
        assert WebDriverWait(login, 10).until(
            EC.text_to_be_present_in_element(Locators.button_checkout, 'Оформить заказ'))
