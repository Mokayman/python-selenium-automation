from pages.base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):

    SIGNIN_TEXT = (By.XPATH, "// h1 [ @ class = 'a-spacing-small']")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")

    def verify_sign_in_text(self):
        self.wait_for_url_contains('https://www.amazon.com/ap/signin?')
        expected_text = 'Sign in'
        self.verify_element_text('Sign in', *self.SIGNIN_TEXT)

    def verify_email_field(self):
        self.verify_element_displayed(*self.EMAIL_FIELD)

