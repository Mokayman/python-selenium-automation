from pages.base_page import Page
from selenium.webdriver.common.by import By



class MainPage(Page):

    CART_ICON = (By.ID, 'nav-cart-count-container')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)




