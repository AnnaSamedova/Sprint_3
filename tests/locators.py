from selenium.webdriver.common.by import By


class Locators:

    # Поле "Имя" в форме регистрации
    reg_name = (By.XPATH, '//label[text()="Имя"]/following-sibling::input[contains(@name, "name")]')

    # Поле "Email" в форме регистрации
    reg_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input[contains(@name, "name")]')

    # Поле "Пароль" в форме регистрации
    reg_password = (By.XPATH, '//input[contains(@type, "password") and contains(@name, "Пароль")]')

    # Кнопка регистрации в форме регистрации
    reg_button = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')

    # Ошибка для некорректного пароля
    reg_error = (By.XPATH, '//p[contains(@class, "input__error") or contains(text(), "Некорректный пароль")]')

    # Кнопка "Войти в аккаунт" на главной странице
    button_auth_home_page = (By.XPATH, '//button[contains(text(), "Войти")]')

    # Поле "Email" в форме авторизации (by.name)
    auth_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input[contains(@name, "name")]')

    # Поле "Пароль" в форме авторизации (by.name)
    auth_password = (By.XPATH, '//input[contains(@type, "password") and contains(@name, "Пароль")]')

    # Кнопка "Войти" в форме авторизации
    auth_button = (By.XPATH, '//button[contains(text(), "Войти")]')

    # Кнопка "Личный кабинет" в правом верхнем углу
    button_account = (By.XPATH, '//a[@href="/account"]')

    # Кнопка "Выход" в личном кабинете
    button_logout = (By.XPATH, '//button[contains(@class, "Account_button__14Yp3") or contains(text(), "Выход")]')

    # Кнопка "Войти" в форме регистрации и восстановления пароля
    button_auth_reg_page = (By.XPATH, '//a[@href="/login"]')

    # Логотип сайта "Stellar burgers" (by.tag_name)
    logo = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo__2D0X2")]')

    # Кнопка перехода в раздел "Конструктор"
    constructor = (By.XPATH, '//p[contains(text(), "Конструктор")]')

    # Раздел "Соусы"
    section_sauce = (By.XPATH, '//div/span[contains(text(), "Соусы")]')

    # Раздел "Начинки"
    section_toppings = (By.XPATH, '//div/span[contains(text(), "Начинки")]')

    # Раздел "Булки"
    section_bread = (By.XPATH, '//div/span[contains(text(), "Булки")]')

    # Кнопка "Оформить заказ" на главной странице
    button_checkout = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')

    # Текст в "Личном кабинете" о возможности редактирования данных
    text_personal_data = (By.XPATH, '//p[contains(text(), "персональные данные")]')

    # Ингредиент раздела "Булки"
    ingredient_bread = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')

    # Ингредиент раздела "Соусы"
    ingredient_sauce = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]')

    # Ингредиент раздела "Начинки"
    ingredient_toppings = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')
