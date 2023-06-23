from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_NAME = (By.ID, "productTitle")
ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
NO_PROTECTION_BTN = (By.ID, "attachSiNoCoverage")


@given('amazon product {product_id} details page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@given('Open amazon fashion {url}')
def open_amazon_fashion_page(context, url):
    context.app.main_page.open_page(url)


@when('store product name')
def store_product_name(context):
    # context.product_name = context.driver.find_element(*PRODUCT_NAME).text

    context.product_name_in_search = context.app.search_results_page.store_product_name()


@when('click on add 2 cart')
def add_to_cart(context):
    context.app.search_results_page.add_to_cart()
    # context.driver.find_element(*ADD_TO_CART_BTN).click()


# context.driver.wait.until(EC.element_to_be_clickable(NO_PROTECTION_BTN), message="BTN not available").click()
# context.app.cart_page.add_to_cart()

@when('Hovers over New Arrivals')
def hovers_over_new_arrivals(context):
    context.app.fashion_page.hovers_over_new_arrivals()


@then('Varify users click through colors')
def users_can_select_colors(context):
    expected_colors = ['01 Black', '02 Navy', '03 White', '04 Wine Red', '05 Light Gray',
                       '06 Khaki', 'Long Sleeve Black', 'Long Sleeve Light Gray', 'Long Sleeve Navy',
                       'Long Sleeve Wine Red', 'Long Sleeve Khaki', 'Long Sleeve White']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for element in colors:
        element.click()
        curent_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [curent_color]

    assert actual_colors == expected_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'


@then('Verify that user sees the deals')
def verify_deals(context):
    context.app.search_results_page.verify_deals()