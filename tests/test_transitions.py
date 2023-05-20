from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


# Тестируемый класс - Переходы
class TestTransitions:

    # Тест №1 - Переход в личный кабинет по клику на «Личный кабинет»
    def test_go_to_personal_account_by_click_on_personal_account(self, login):
        login.find_element(By.XPATH, Locators.button_account).click()
        WebDriverWait(login, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_logout)))

    # Тест №2 - Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_go_to_constructor_from_personal_account_by_click_on_logo(self, login):
        login.find_element(By.XPATH, Locators.button_account).click()
        login.find_element(By.TAG_NAME, Locators.logo).click()
        WebDriverWait(login, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_checkout)))

    # Тест №3 - Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_go_to_constructor_from_personal_account_by_click_on_constructor(self, login):
        login.find_element(By.XPATH, Locators.button_account).click()
        login.find_element(By.XPATH, Locators.constructor).click()
        WebDriverWait(login, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_checkout)))
