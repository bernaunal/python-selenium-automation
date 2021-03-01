from behave import given, when, then
from selenium.webdriver.common.by import By


BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')

@given('Open Amazon Prime page')
def open_Amazon(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify 8 benefit boxes are displayed')
def Verify_benefit_boxes(box_count, context):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == int(box_count), f'Expected {box_count} boxes but we see {len(actual_boxes)}'

