from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):

    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    ALL_SEARCH_RESULTS_IMAGE = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] .s-image ")
    PRODUCT_NAME_IN_SEARCH = (By.ID, "productTitle")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    NO_PROTECTION_BTN = (By.ID, "attachSiNoCoverage")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

    def click_first_result(self):
        self.click(*self.ALL_SEARCH_RESULTS_IMAGE)

    def store_product_name(self):
        self.product_name_in_search = self.find_element(*self.PRODUCT_NAME_IN_SEARCH).text

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_for_element_click(*self.NO_PROTECTION_BTN)
