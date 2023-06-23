from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By



class MainPage(Page):

    CART_ICON = (By.ID, 'nav-cart-count-container')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')

    def open_page(self, link):
        self.open_url(link)
        sleep(5)
    def open_fashion_page(self):
        self.open_url('https://www.amazon.com/amazon-fashion/b/?ie=UTF8&node=7141123011&ref_=topnav_storetab_sl')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)




