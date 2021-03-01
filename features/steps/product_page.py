from behave import given, when, then
from selenium.webdriver.common.by import By


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify cart has {expected_count} item')
def verify_item_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count}'


@given('Open Amazon Dress B07ZKLBLL4 page')
def open_amazon_dress(context):
    context.driver.get("https://www.amazon.com/SheIn-Womens-Elegant-Sleeve-Pocket/dp/B07ZKLBLL4/ref=sr_1_1?dchild=1&keywords=B07ZKLBLL4&qid=1614634963&sr=8-1")


@then('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ['Black', 'Green', 'Burgundy#2']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    # [Webelement 0, Webelement 1, Webelement 2]

    # for color in colors:
    #     color.click()

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]} but got {selected_color}'

