from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.NAME, 'help_keywords')
RESULTS = (By.XPATH, "//div[@class='help-content']/h1")


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into search field in Help')
def input_cancel(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys('Cancel Orders', Keys.RETURN)
    sleep(4)


@then('First result should contain {search_word}')
def check_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)
