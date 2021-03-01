from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINKS = (By.CSS_SELECTOR, 'div#zg_tabs a')


@given('Open Amazon Best Seller page')
def open_Amazon_Best_Seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


# @then('Searching for {search_word}')
# def input_search(context, search_word):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)

@then('Verify there are {link_count} links')
def Verify_links_count(context, link_count):
    actual_links = context.driver.find_elements(*LINKS)
    actual_links_count = len(actual_links)
    assert actual_links_count == int(link_count), f'Expected {link_count} links but we see {actual_links_count}'

