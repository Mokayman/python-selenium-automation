from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('click on returns_and_orders')
def click_on_returns(context):
    context.driver.find_element(By.XPATH, "//span[text()='Returns']").click()


@then("Verify 'Sign in' text is shown on the page")
def verify_sign_in_text(context):
    actual_result = context.driver.find_element(By.XPATH, "// h1 [ @ class = 'a-spacing-small']").text
    expected_result = "Sign in"
    assert expected_result == actual_result, f"expected {expected_result} but got {actual_result}"


@then("Verify email field is shown on the page")
def verify_email_field(context):
    assert context.driver.find_element(By.XPATH, "//input[@type='email']").is_displayed(), "email field not shown"


@when('click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite").click()


@then("Verify 'Your Amazon Cart is empty' text is shown on the page")
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f"expected {expected_result} but got {actual_result}"


@then("Verify Sign in to your account button is shown on the page")
def verify_sign_in_button(context):
    context.driver.find_element(By.ID, "a-autoid-0").is_displayed(), "Sign in to your account button not shown"

