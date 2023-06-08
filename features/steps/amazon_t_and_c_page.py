from selenium.webdriver.common.by import By
from behave import given, when, then
# from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[href *= 'https://www.amazon.com/privacy']")

@given('Open Amazon Terms and Conditions page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()

