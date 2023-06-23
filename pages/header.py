from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURN_BTN = (By.XPATH, "//span[text()='Returns']")
    LANGUAGE_OPTION = (By.CSS_SELECTOR, "#nav-tools span[class = 'icp-nav-link-inner']")
    SPANISH_RADIO_BTN = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEP_SELECT = (By.ID, 'searchDropdownBox')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_on_returns(self):
        self.click(*self.RETURN_BTN)

    def hover_over_language_options(self):
        language_opt_element = self.find_element(*self.LANGUAGE_OPTION)
        action = ActionChains(self.driver)

        action.move_to_element(language_opt_element)
        action.perform()

    def verify_spanish_language(self):
        self.wait_for_element_appear(*self.SPANISH_RADIO_BTN)

    def select_department(self, department_name):
        dep_select_element = self.find_element(*self.DEP_SELECT)
        select = Select(dep_select_element)

        select.select_by_value(department_name)


