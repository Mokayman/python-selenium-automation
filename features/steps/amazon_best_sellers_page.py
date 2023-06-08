from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLERS_MENU = (By.CSS_SELECTOR, ".nav-a[href *= 'bestsellers']")
BEST_SELLERS_LINKS =(By.CSS_SELECTOR, "#zg_header li")
HEADER_BANNER_TEXT = (By.ID, "zg_banner_text")



@when("Click on Best Sellers menu")
def click_best_ellers(context):
    context.driver.find_element(*BEST_SELLERS_MENU).click()


@then("Verify the {links} header links")
def verify_5_links(context, links):
    link_count = len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    link_count = link_count
    assert link_count == int(links)


@then('Clicks on each top link and verifies that correct page opens')
def click_verify_bs_links(context):
    links = context.driver.find_elements(*BEST_SELLERS_LINKS)

    for index in range(len(links)):
        current_link = context.driver.find_elements(*BEST_SELLERS_LINKS)[index]
        link_text = current_link.text
        current_link.click()

        header_text = context.driver.find_element(*HEADER_BANNER_TEXT).text

        assert link_text in header_text, f"Expected {link_text} is not in {header_text}"



