from selenium.webdriver.common.by import By
from behave import given, when, then


CUSTOMER_SERVICES_BTN = (By.CSS_SELECTOR, ".nav-a[href *= 'nav_cs_customerservice']")
WELCOME_TO_AMAZON_TXT = (By.XPATH, "//h1[text() = 'Welcome to Amazon Customer Service']")
HELP_OPTIONS = (By.CSS_SELECTOR, ".issue-card-wrapper")
HELP_LIBRARY_TXT = (By.XPATH, "//h2[text() = 'Search our help library']")
HELP_SEARCH_BOX = (By.ID, "hubHelpSearchInput")
HELP_TOPICS_TXT = (By.XPATH, "//h2[text() = 'All help topics']")
HELP_TOPICS_OPTIONS = (By.CSS_SELECTOR, "li.help-topics")


@when('Click on Customer Service menu')
def click_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICES_BTN).click()


@then('verify Customer Service’s page UI elements are present')
def verify_customer_sevices_ui(context):
    # Verify page header title
    actual_result = context.driver.find_element(*WELCOME_TO_AMAZON_TXT).text
    expected_result = "Welcome to Amazon Customer Service"
    assert actual_result == expected_result, f"expected {expected_result} but found {actual_result}"


    # Verify help options
    help_option_count = len(context.driver.find_elements(*HELP_OPTIONS))
    assert help_option_count == 10, f" expected 10 but found {help_option_count}"


    # Verify Search our help library text
    actual_result = context.driver.find_element(*HELP_LIBRARY_TXT).text
    expected_result = "Search our help library"
    assert actual_result == expected_result, f"expected {expected_result} but found {actual_result}"


    # Verify help search text box
    context.driver.find_element(*HELP_SEARCH_BOX).is_displayed(), "help search text box not shown"


    # Verify All help topics text
    actual_result = context.driver.find_element(*HELP_TOPICS_TXT).text
    expected_result = "All help topics"
    assert actual_result == expected_result, f"expected {expected_result} but found {actual_result}"

    # Verify All help topic  options
    help_option_count = len(context.driver.find_elements(*HELP_TOPICS_OPTIONS))
    assert help_option_count == 11, f" expected 10 but found {help_option_count}"

