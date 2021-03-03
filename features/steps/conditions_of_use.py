from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


AMAZON_APPS = (By.CSS_SELECTOR, "a[href *= 'feature.html']")
DOWNLOAD_APP_LINK = (By.ID, 'mgt-email-sms-download-header')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon applications link')
def click_on_amazon_apps(context):
    context.driver.find_element(*AMAZON_APPS).click()


@then('Amazon app page is opened')
def amazon_app_page_is_opened(context):
    context.driver.wait.until(EC.element_to_be_clickable(DOWNLOAD_APP_LINK))


