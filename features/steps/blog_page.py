from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@when('Switch to new window')
def new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.all_windows = context.driver.window_handles
    context.new_window = context.driver.switch_to.window(context.all_windows[1])
    print(context.all_windows)


@then('Verify blog is open')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains("https://www.aboutamazon.com/news/workplace/meet-the-dogs-of-amazon?"))


@then('close blog')
def close_blog(context):
    context.driver.close()
