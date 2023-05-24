from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_stellar_burgers = "https://stellarburgers.nomoreparties.site"


class TestSectionConstructor:

    def test_go_to_section_toppings_in_the_constructor(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(*Locators.section_toppings).click()
        element_toppings = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.ingredient_toppings)).text
        expected_text_toppings = "Мясо бессмертных моллюсков Protostomia"
        assert expected_text_toppings in element_toppings

    def test_go_to_section_sauce_in_the_constructor(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(*Locators.section_sauce).click()
        element_sauce = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.ingredient_sauce)).text
        expected_text_sauce = "Соус Spicy-X"
        assert expected_text_sauce in element_sauce

    def test_go_to_section_bread_in_the_constructor(self, browser):
        browser.get(link_stellar_burgers)
        browser.find_element(*Locators.section_toppings).click()
        browser.find_element(*Locators.section_bread).click()
        element_bread = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.ingredient_bread)).text
        expected_text_bread = "Флюоресцентная булка R2-D3"
        assert expected_text_bread in element_bread
