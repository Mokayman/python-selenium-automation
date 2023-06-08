from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_QUANTITY = (By.ID, "nav-cart-count")
PRODUCT_NAME = (By.CSS_SELECTOR, ".a-truncate-cut")


@then('varify cart has one item(s)')
def varify_cart_count(context):
    cart_count = int(context.driver.find_element(*CART_QUANTITY).text)
    assert cart_count == 1, f"cart has {cart_count}"


@then("varify product name")
def varify_product_name(context):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in product_name_in_cart
