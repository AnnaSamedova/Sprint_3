from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_registration_form = "https://stellarburgers.nomoreparties.site/register"


# Тестируемый класс - Регистрация
class TestRegistration:

    # Тест №1 - Успешная регистрация
    def test_successful_registration(self, browser, fake_name, fake_email, fake_password):
        browser.get(link_registration_form)
        browser.find_element(By.XPATH, Locators.reg_name).send_keys(fake_name)
        browser.find_element(By.XPATH, Locators.reg_email).send_keys(fake_email)
        browser.find_element(By.XPATH, Locators.reg_password).send_keys(fake_password)
        browser.find_element(By.XPATH, Locators.reg_button).click()

    # Тест №2 - Ошибка для некорректного пароля
    def test_error_for_invalid_password(self, browser, fake_name, fake_email):
        browser.get(link_registration_form)
        browser.find_element(By.XPATH, Locators.reg_name).send_keys(fake_name)
        browser.find_element(By.XPATH, Locators.reg_email).send_keys(fake_email)
        browser.find_element(By.XPATH, Locators.reg_password).send_keys('1')
        browser.find_element(By.XPATH, Locators.reg_button).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.reg_error)))
