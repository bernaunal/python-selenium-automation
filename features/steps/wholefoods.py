from behave import given, then
from selenium.webdriver.common.by import By


PRODUCTS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class, 'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")


@given('Open Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify products have regular prices and names')
def verify_regular_price_and_names(context):
    product_elements = context.driver.find_elements(*PRODUCTS)
    for e in product_elements:
        assert 'Regular' in e.text, f'Error...'
        product_name = e.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Error...'


