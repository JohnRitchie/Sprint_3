import uuid
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPage, RegistrationPage, AuthenticationPage
import links


def get_uuid():
    return str(uuid.uuid4())


def get_email_address():
    return f'{get_uuid()}@{get_uuid()}.com'


def wait_element_located(browser, element):
    WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(element))


def register_new_user(browser):
    email_address = get_email_address()
    password = get_uuid()

    browser.get(links.REGISTER_LINK)
    browser.find_element(*RegistrationPage.LOGIN_NAME).send_keys(get_uuid())
    browser.find_element(*RegistrationPage.LOGIN_EMAIL).send_keys(email_address)
    browser.find_element(*RegistrationPage.LOGIN_PASSWORD).send_keys(password)
    browser.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

    wait_element_located(browser, AuthenticationPage.LOGIN_BUTTON)
    assert browser.current_url == links.LOGIN_LINK

    return email_address, password


def authenticate_user(browser, email_address, password):
    assert browser.current_url == links.LOGIN_LINK

    browser.find_element(*AuthenticationPage.LOGIN_EMAIL).send_keys(email_address)
    browser.find_element(*AuthenticationPage.LOGIN_PASSWORD).send_keys(password)
    browser.find_element(*AuthenticationPage.LOGIN_BUTTON).click()

    wait_element_located(browser, MainPage.ORDER_BUTTON)
    assert browser.current_url == links.MAIN_LINK
