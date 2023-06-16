from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
ALL_SEARCH_RESULTS_IMAGE = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] .s-image ")
RESULTS_PRODUCT_NAME = (By.CSS_SELECTOR, "h2")
ALL_SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")


@when('click on the first product')
def click_first_result(context):
    # context.driver.find_element(*ALL_SEARCH_RESULTS_IMAGE).click()
    context.app.search_results_page.click_first_result()


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    # actual_result = context.driver.find_element(*RESULT_TEXT).text
    # assert expected_result == actual_result, \
    #     f'Error! Expected {expected_result} bot got actual {actual_result}'
    context.app.search_results_page.verify_search_results(expected_result)


@then('Verify search results has image and product name')
def verify_image_and_product_name(context):
    all_search_results = context.driver.find_elements(*ALL_SEARCH_RESULTS)

    for product in all_search_results:
        product_name = product.find_element(*RESULTS_PRODUCT_NAME).text
        # print(f'* {product_name}')
        assert product_name != "", "No product name found"
        assert product.find_element(*ALL_SEARCH_RESULTS_IMAGE).is_displayed(), "image not found"
#