from selenium.webdriver.common.by import By
from behave import given, when, then

BEST_SELLERS_MENU = (By.CSS_SELECTOR, ".nav-a[href *= 'bestsellers']")
BEST_SELLERS_LINKS =(By.XPATH, "//div[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs')]")
@when("Click on Best Sellers menu")
def click_best_ellers(context):
    context.driver.find_element(*BEST_SELLERS_MENU).click()


@then("Verify the {links} header links")
def verify_5_links(context, links):
    link_count = len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    link_count = link_count - 1
    assert link_count == int(links)

