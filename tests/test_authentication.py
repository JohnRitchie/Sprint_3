import links
from locators import MainPage, AuthenticationPage, ForgotPasswordPage
from helpers import register_new_user, authenticate_user, wait_element_located


def test_authentication_from_registration_page_right_data_success(browser):
    email_address, password = register_new_user(browser)
    authenticate_user(browser, email_address, password)


def test_authentication_from_main_page_login_button_right_data_success(browser):
    email_address, password = register_new_user(browser)

    browser.get(links.MAIN_LINK)
    browser.find_element(*MainPage.LOGIN_BUTTON).click()

    wait_element_located(browser, AuthenticationPage.LOGIN_BUTTON)

    authenticate_user(browser, email_address, password)


def test_authentication_from_main_page_personal_account_button_right_data_success(browser):
    email_address, password = register_new_user(browser)

    browser.get(links.MAIN_LINK)
    browser.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()

    wait_element_located(browser, AuthenticationPage.LOGIN_BUTTON)

    authenticate_user(browser, email_address, password)


def test_authentication_from_forgot_password_page_right_data_success(browser):
    email_address, password = register_new_user(browser)

    browser.get(links.FORGOT_PASSWORD_LINK)
    browser.find_element(*ForgotPasswordPage.LOGIN_BUTTON).click()

    wait_element_located(browser, AuthenticationPage.LOGIN_BUTTON)

    authenticate_user(browser, email_address, password)
