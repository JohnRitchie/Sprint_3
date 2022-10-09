from locators import ConstructorPage
from helpers import register_new_user, authenticate_user


def test_constructor_go_to_rolls_section_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    # при входе на главную выбран раздел "Булки", поэтому он не кликабелен
    browser.find_element(*ConstructorPage.SAUCES_BUTTON).click()
    browser.find_element(*ConstructorPage.ROLLS_BUTTON).click()

    current_section_name = browser.find_element(*ConstructorPage.CURRENT_SECTION).text

    assert current_section_name == 'Булки'


def test_constructor_go_to_sauces_section_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*ConstructorPage.SAUCES_BUTTON).click()

    current_section_name = browser.find_element(*ConstructorPage.CURRENT_SECTION).text

    assert current_section_name == 'Соусы'


def test_constructor_go_to_fillings_section_success(browser):
    authenticate_user(browser, *register_new_user(browser))

    browser.find_element(*ConstructorPage.FILLINGS_BUTTON).click()

    current_section_name = browser.find_element(*ConstructorPage.CURRENT_SECTION).text

    assert current_section_name == 'Начинки'
