from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FashionPage(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals']")

    def hovers_over_new_arrivals(self):
        new_arrivals_element = self.find_element(*self.NEW_ARRIVALS)
        action = ActionChains(self.driver)

        action.move_to_element(new_arrivals_element)
        action.perform()



