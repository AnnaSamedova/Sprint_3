from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


# Тестируемый класс - Выход из аккаунта
class TestLogout:

    # Тест №1 - Выход из аккаунта по кнопке "Выйти" в личном кабинете
    def test_logout(self, login):
        login.find_element(By.XPATH, Locators.button_account).click()
        WebDriverWait(login, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_logout))).click()
        WebDriverWait(login, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.auth_button)))
