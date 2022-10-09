from selenium.webdriver.common.by import By


class Common:
    WRONG_PASSWORD_MESSAGE = (By.XPATH, './/p[text()="Некорректный пароль"]')
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]')


class MainPage(Common):
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')


class RegistrationPage(Common):
    LOGIN_NAME = (By.CSS_SELECTOR, '.Auth_form__3qKeq .Auth_fieldset__1QzWN:nth-child(1) div div input')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '.Auth_form__3qKeq .Auth_fieldset__1QzWN:nth-child(2) div div input')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '.Auth_form__3qKeq .Auth_fieldset__1QzWN:nth-child(3) div div input')
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')


class AuthenticationPage(Common):
    LOGIN_EMAIL = (By.CSS_SELECTOR, '.Auth_form__3qKeq .Auth_fieldset__1QzWN:nth-child(1) div div input')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '.Auth_form__3qKeq .Auth_fieldset__1QzWN:nth-child(2) div div input')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')


class ForgotPasswordPage(Common):
    LOGIN_BUTTON = (By.XPATH, './/a[text()="Войти"]')


class PersonalAccountPage(Common):
    SAVE_BUTTON = (By.XPATH, './/button[text()="Сохранить"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')


class ConstructorPage(Common):
    ROLLS_BUTTON = (By.XPATH, './/span[text()="Булки"]')
    SAUCES_BUTTON = (By.XPATH, './/span[text()="Соусы"]')
    FILLINGS_BUTTON = (By.XPATH, './/span[text()="Начинки"]')
    CURRENT_SECTION = (By.XPATH, './/div[contains(@class,"current")]/span')
