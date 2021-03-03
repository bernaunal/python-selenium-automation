from time import sleep
from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
NAV_TOOL = (By.ID, 'nav-tools')

@when('Click Sign In from popup')
def click_sign_in_popup_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    e.click()


@then('Verify Sign In page opens')
def verify_sign_in_page_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                              f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin')
    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url,    \
    #     f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'


@then('Verify sign in is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))


@when('Wait for {sec} sec')
def Wait_for_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In disappears')
def verify_sign_in_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN))
    # context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    context.driver.find_element(*NAV_TOOL)
    # context.driver.wait.until(EC.presence_of_element_located(NAV_TOOL))

