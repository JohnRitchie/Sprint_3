import links
from locators import MainPage, PersonalAccountPage, AuthenticationPage
from helpers import register_new_user, authenticate_user, wait_element_located


def test_personal_account_enter_from_main_page_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()

    wait_element_located(browser, PersonalAccountPage.SAVE_BUTTON)

    assert browser.current_url == links.PERSONAL_ACCOUNT_LINK


def test_personal_account_with_constructor_button_to_main_page_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
    wait_element_located(browser, PersonalAccountPage.SAVE_BUTTON)

    browser.find_element(*PersonalAccountPage.CONSTRUCTOR_BUTTON).click()

    wait_element_located(browser, MainPage.ORDER_BUTTON)

    assert browser.current_url == links.MAIN_LINK


def test_personal_account_with_logo_button_to_main_page_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
    wait_element_located(browser, PersonalAccountPage.SAVE_BUTTON)

    browser.find_element(*PersonalAccountPage.LOGO_BUTTON).click()

    wait_element_located(browser, MainPage.ORDER_BUTTON)

    assert browser.current_url == links.MAIN_LINK


def test_personal_account_exit_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
    wait_element_located(browser, PersonalAccountPage.SAVE_BUTTON)

    browser.find_element(*PersonalAccountPage.EXIT_BUTTON).click()

    wait_element_located(browser, AuthenticationPage.LOGIN_BUTTON)

    assert browser.current_url == links.LOGIN_LINK
