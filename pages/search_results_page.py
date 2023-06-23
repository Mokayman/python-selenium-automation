from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class SearchResultsPage(Page):

    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    ALL_SEARCH_RESULTS_IMAGE = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] .s-image ")
    PRODUCT_NAME_IN_SEARCH = (By.ID, "productTitle")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    NO_PROTECTION_BTN = (By.ID, "attachSiNoCoverage")
    BOOKS_SUBMENU = (By.CSS_SELECTOR, "[data-category='books']")
    FASHION_SUBMENU = (By.ID, 'nav-subnav')
    NEW_ARRIVALS_SUBMENU = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/']")
    DEALS_MEN = (By.XPATH, "//a[@class='mm-merch-panel'] //h3[contains(text(), 'Men')]")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_for_element_click(*self.NO_PROTECTION_BTN)

    def click_first_result(self):
        self.click(*self.ALL_SEARCH_RESULTS_IMAGE)

    # def hovers_over_new_arrivals(self):


    def store_product_name(self):
        return self.find_element(*self.PRODUCT_NAME_IN_SEARCH).text


    def verify_department(self):
        self.verify_element_displayed(*self.BOOKS_SUBMENU)

    def verify_men_department(self):
        self.verify_element_displayed(*self.FASHION_SUBMENU)
    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS_MEN)