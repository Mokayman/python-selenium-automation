from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

DOG_IMAGE = (By.ID, 'd')
@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on a dog image')
def click_on_dog_image(context):
    context.driver.find_element(*DOG_IMAGE).click()



@then('Return to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)

