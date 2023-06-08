

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CART = (By.ID, "nav-cart")
NO_PROTACTION_BTN = (By.ID, "attachSiNoCoverage")


@when('open cart page')
def open_cart(context):

    # context.driver.find_element(*NO_PROTACTION_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(NO_PROTACTION_BTN), message="BTN not avalable")
    context.driver.find_element(*NO_PROTACTION_BTN).click()
    # context.driver.find_element(*CART).click()
    context.driver.wait.until(EC.element_to_be_clickable(CART)).click()

