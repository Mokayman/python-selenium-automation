from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_TEXT = (By.XPATH, "//h1[text() = 'Amazon.com Privacy Notice']")


@when('Switch to the newly opened window')
def switch_2new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.all_windows = context.driver.window_handles
    context.new_window = context.driver.switch_to.window(context.all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page(context):
    expected_text = "Amazon.com Privacy Notice"
    actual_text = context.driver.find_element(*PRIVACY_TEXT).text
    assert expected_text == actual_text, f'expected {expected_text} but found {actual_text}'


@then('Verify user can close new window and switch back to original')
def close_switch_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.all_windows[0])
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html/')),\
        "page not found"

