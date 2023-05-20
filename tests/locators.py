from enum import StrEnum


class Locators(StrEnum):

    # Поле "Имя" в форме регистрации
    reg_name = '(.//input[@class="text input__textfield text_type_main-default"])[1]'

    # Поле "Email" в форме регистрации
    reg_email = '(.//input[@class="text input__textfield text_type_main-default"])[2]'

    # Поле "Пароль" в форме регистрации
    reg_password = '(.//input[@class="text input__textfield text_type_main-default"])[3]'

    # Кнопка регистрации в форме регистрации
    reg_button = './/button[text()="Зарегистрироваться"]'

    # Ошибка для некорректного пароля
    reg_error = './/p[text()="Некорректный пароль"]'

    # Кнопка "Войти в аккаунт" на главной странице
    button_auth_home_page = '//button[text()="Войти в аккаунт"]'

    # Поле "Email" в форме авторизации (by.name)
    auth_email = 'name'

    # Поле "Пароль" в форме авторизации (by.name)
    auth_password = 'Пароль'

    # Кнопка "Войти" в форме авторизации
    auth_button = '//button[text()="Войти"]'

    # Кнопка "Личный кабинет" в правом верхнем углу
    button_account = '//p[text()="Личный Кабинет"]'

    # Кнопка "Выход" в личном кабинете
    button_logout = '//button[text()="Выход"]'

    # Кнопка "Войти" в форме регистрации и восстановления пароля
    button_auth_reg_page = '//a[text()="Войти"]'

    # Логотип сайта "Stellar burgers" (by.tag_name)
    logo = 'svg'

    # Кнопка перехода в раздел "Конструктор"
    constructor = '//p[text()="Конструктор"]'

    # Раздел "Соусы"
    section_sauce = '(.//div/span[@class="text text_type_main-default"])[2]'

    # Раздел "Начинки"
    section_toppings = '(.//div/span[@class="text text_type_main-default"])[3]'

    # Раздел "Булки"
    section_bread = '(.//div/span[@class="text text_type_main-default"])[1]'

    # Кнопка "Оформить заказ" на главной странице
    button_checkout = './/button[text()="Оформить заказ"]'
