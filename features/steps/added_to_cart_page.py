from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@when('open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()
