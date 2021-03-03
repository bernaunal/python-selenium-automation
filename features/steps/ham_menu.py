from behave import given, when, then
from selenium.webdriver.common.by import By


HAM_MENU = (By.ID, 'nav-hamburger-menu')

@given('Open Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    e = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()
    context.driver.find_element(*HAM_MENU).click()

