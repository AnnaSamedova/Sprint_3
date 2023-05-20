from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"
link_registration_form = "https://stellarburgers.nomoreparties.site/register"
link_forgot_password = "https://stellarburgers.nomoreparties.site/forgot-password"


# Тестируемый класс - Авторизация
class TestAuthorization:

    # Тест №1 - Вход по кнопке «Войти в аккаунт» на главной
    def test_authorization_by_the_button_login_to_account(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(By.XPATH, Locators.button_auth_home_page).click()
        browser.find_element(By.NAME, Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(By.NAME, Locators.auth_password).send_keys('123456')
        browser.find_element(By.XPATH, Locators.auth_button).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_account))).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_logout)))

    # Тест №2 - Вход через кнопку «Личный кабинет»
    def test_authorization_by_the_button_personal_account(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(By.XPATH, Locators.button_account).click()
        browser.find_element(By.NAME, Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(By.NAME, Locators.auth_password).send_keys('123456')
        browser.find_element(By.XPATH, Locators.auth_button).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_account))).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_logout)))

    # Тест №3 - Вход через кнопку в форме регистрации
    def test_authorization_in_the_registration_form(self, browser):
        browser.get(link_registration_form)
        browser.find_element(By.XPATH, Locators.button_auth_reg_page).click()
        browser.find_element(By.NAME, Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(By.NAME, Locators.auth_password).send_keys('123456')
        browser.find_element(By.XPATH, Locators.auth_button).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_account))).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_logout)))

    # Тест №4 - Вход через кнопку в форме восстановления пароля
    def test_authorization_in_the_password_recovery_form(self, browser):
        browser.get(link_forgot_password)
        browser.find_element(By.XPATH, Locators.button_auth_reg_page).click()
        browser.find_element(By.NAME, Locators.auth_email).send_keys('anna_samedova_10_123@yandex.ru')
        browser.find_element(By.NAME, Locators.auth_password).send_keys('123456')
        browser.find_element(By.XPATH, Locators.auth_button).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_account))).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_logout)))
