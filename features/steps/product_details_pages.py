from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.ID, "productTitle")
ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given('amazon product {product_id} details page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text


@when('click on add 2 cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@then('Varify users click through colors')
def users_can_select_colors(context):
    expected_colors = ['01 Black', '02 Navy', '03 White', '04 Wine Red', '05 Light Gray',
                       '06 Khaki', 'Long Sleeve Black', 'Long Sleeve Light Gray', 'Long Sleeve Navy',
                       'Long Sleeve Wine Red', 'Long Sleeve Khaki', 'Long Sleeve White']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for element in colors:
        element.click()
        curent_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [curent_color]

    assert actual_colors == expected_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'

#

