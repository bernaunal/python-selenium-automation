from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

DOG_IMG = (By.CSS_SELECTOR, "a[href='/dogsofamazon'] img")

@given('Open Amazon Dress B07ZKSSSLBLL4 page')
def open_amazon_dress(context):
    context.driver.get("https://www.amazon.com/SheIn-Womens-Elegant-Sleeve-Pocket/dp/B07ZAASSKLBLL4/ref=sr_1_1?dchild=1&keywords=B07ZKLBLL4&qid=1614634963&sr=8-1")


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle
    # store it in Behave's context to be able to make it global
    print(context.original_window)
    # sleep(2)


@when('Click to open blog')
def click_to_open_blog(context):
    context.driver.find_element(*DOG_IMG).click()
    # sleep(2)


@when('Switch to the newly opened window')
def switch_to_blog(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to_window(context.driver.window_handles[1])


@then('User can close new window and switch')
def close_old_to_switch(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)

