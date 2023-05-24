from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

link_page_login = "https://stellarburgers.nomoreparties.site/login"


class TestLogout:

    def test_logout_with_button_logout_in_the_personal_account(self, login):
        login.find_element(*Locators.button_account).click()
        WebDriverWait(login, 10).until(EC.element_to_be_clickable(Locators.button_logout)).click()
        WebDriverWait(login, 5).until(EC.presence_of_element_located(Locators.auth_button))
        current_url = login.current_url
        assert current_url == link_page_login
