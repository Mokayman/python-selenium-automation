from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
from selenium.webdriver.support import expected_conditions as EC


RETURN_BTN = (By.XPATH, "//span[text()='Returns']")
CART_ICON = (By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite")
SIGNIN_TEXT = (By.XPATH, "// h1 [ @ class = 'a-spacing-small']")
EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
SIGNIN_BTN = (By.ID, "a-autoid-0")


# @when('click on returns_and_orders')
# def click_on_returns(context):
#     context.driver.find_element(*RETURN_BTN).click()
#     # context.app.header.click_on_returns()



@when('click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@then("Verify 'Sign in' text is shown on the page")
def verify_sign_in_text(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?'))
    # actual_result = context.driver.find_element(SIGNIN_TEXT).text
    # expected_result = "Sign in"
    # assert expected_result == actual_result, f"expected {expected_result} but got {actual_result}"
    context.app.signin_page.verify_sign_in_text()

@then("Verify email field is shown on the page")
def verify_email_field(context):
    # assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), "email field not shown"
    context.app.signin_page.verify_email_field()



@then("Verify 'Your Amazon Cart is empty' text is shown on the page")
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f"expected {expected_result} but got {actual_result}"


@then("Verify Sign in to your account button is shown on the page")
def verify_sign_in_button(context):
    context.driver.find_element(*SIGNIN_BTN).is_displayed(), "Sign in to your account button not shown"


