from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
SIGN_IN_POPUP_BTN = (By.ID, "nav-signin-tooltip")

@given('Open amazon main page')
def open_main_page(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()



@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).is_displayed()


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 36
    print(type(links_count))

    # 36 == 36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'


@when('Click sign in')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    context.driver.find_element(*SIGN_IN_POPUP_BTN).click()


@when("Wait for {sec} seconds")
def wait(context, sec):
    sleep(int(sec))


@then("Verify sign in button is clickable")
def verify_signin_btn_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN)), 'Signin button not clickable'

@then("Verify Sign in popup disappears")
def verify_signin_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN)), 'Signin button does not disappear'
