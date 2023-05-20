from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"


# Тестируемый класс - Раздел "Конструктор"
class TestSectionConstructor:

    # Тест №1 - Переход к разделу «Соусы»
    def test_go_to_section_sauce(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(By.XPATH, Locators.section_sauce).click()

    # Тест №2 - Переход к разделу "Начинки"
    def test_go_to_section_toppings(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(By.XPATH, Locators.section_toppings).click()

    # Тест №3 - Переход к разделу «Булки»
    def test_go_to_section_bread(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(By.XPATH, Locators.section_toppings).click()
        browser.find_element(By.XPATH, Locators.section_bread).click()
