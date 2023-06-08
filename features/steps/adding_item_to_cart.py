from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import Select
@when('click on the search bar and populate with {item}')
def search_and_populate(context, item):
    context.driver.find_element(By.ID, "twotabsearchtextbox").click()
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(item)

@when('click on the search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@when('click on the desired item')
def click_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[data-image-index='12']").click()


@when('click on the shopping cart icon')
def click_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite")


@when("varify cart is empty")
def varify_cart_empty(context):
    items_on_cart = context.driver.find_element(By.ID, "a-autoid-1-announce").text
    print(items_on_cart)
    assert items_on_cart != '0', "there is already an item on cart"


@when('click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then('Verify shopping cart contains one item')
def varify_cart_item(context):
    items_on_cart = context.driver.find_element(By.ID, "nav-cart-count").text
    assert items_on_cart == "1", "items on cart is more than one"
