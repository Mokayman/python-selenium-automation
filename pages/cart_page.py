from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#sc-active-cart h2")
    CART = (By.ID, "nav-cart")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    CART_QUANTITY = (By.ID, "nav-cart-count")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".a-truncate-cut")
    NO_PROTECTION_BTN = (By.ID, "attachSiNoCoverage")
    PROCEED_CHECKOUT = (By.ID, 'sc-buy-box-ptc-button')

    def verify_empty_cart(self):
        self.verify_element_text('Your Amazon Cart is empty', *self.EMPTY_CART_TEXT)

    def varify_cart_count(self):
        self.verify_element_int(1, *self.CART)

    def varify_product_name(self, product_name_in_search):
        self.verify_partial_text(product_name_in_search, *self.PRODUCT_NAME_IN_CART)


    def open_cart(self):
        # self.wait_for_element_appear(*self.PROCEED_CHECKOUT)
        self.wait_for_element_click(*self.CART)
