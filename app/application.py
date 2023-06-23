from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import Signin
from pages.cart_page import CartPage
from pages.fashion_page import FashionPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = Signin(self.driver)
        self.cart_page = CartPage(self.driver)
        self.fashion_page = FashionPage(self.driver)




