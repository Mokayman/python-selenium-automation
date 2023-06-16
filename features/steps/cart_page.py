from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_QUANTITY = (By.ID, "nav-cart-count")
PRODUCT_NAME = (By.CSS_SELECTOR, ".a-truncate-cut")


@then('varify cart has one item(s)')
def varify_cart_count(context):
    # cart_count = int(context.driver.find_element(*CART_QUANTITY).text)
    # assert cart_count == 1, f"cart has {cart_count}"
    context.app.cart_page.varify_cart_count()

@then("varify product name")
def varify_product_name(context):
    context.app.cart_page.varify_product_name()
    # product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    # assert context.product_name[:30] in product_name_in_cart


@then('Verify \'Your Amazon Cart is empty\'. text present')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()
