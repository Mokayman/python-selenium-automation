from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):

    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURN_BTN = (By.XPATH, "//span[text()='Returns']")

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_on_returns(self):
        self.click(*self.RETURN_BTN)


