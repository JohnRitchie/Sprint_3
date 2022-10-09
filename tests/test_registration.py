import links
from locators import RegistrationPage
from helpers import register_new_user, get_uuid, get_email_address, wait_element_located


def test_registration_right_data_success(browser):
    register_new_user(browser)


def test_registration_wrong_password_error(browser):
    browser.get(links.REGISTER_LINK)
    browser.find_element(*RegistrationPage.LOGIN_NAME).send_keys(get_uuid())
    browser.find_element(*RegistrationPage.LOGIN_EMAIL).send_keys(get_email_address())
    browser.find_element(*RegistrationPage.LOGIN_PASSWORD).send_keys('wrong')
    browser.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

    wait_element_located(browser, RegistrationPage.WRONG_PASSWORD_MESSAGE)
    assert browser.current_url == links.REGISTER_LINK
