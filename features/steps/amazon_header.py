from behave import when, then, given


@when('Search for {search_query}')
def search_amazon(context, search_query):
    # context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon(search_query)


@when('Populate with {item} and click search')
def search_amazon(context, item):
    context.app.header.search_amazon(item)


@when('click on returns_and_orders')
def click_on_returns(context):
    # context.driver.find_element(*RETURN_BTN).click()
    context.app.header.click_on_returns()


@when("Click on cart icon")
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@when("Hover over language options")
def hover_over_language_options(context):
    context.app.header.hover_over_language_options()


@when('Select department books {department_name}')
def select_department(context, department_name):
    context.app.header.select_department(department_name)


@when('Select department men {department_name}')
def select_department(context, department_name):
    context.app.header.select_department(department_name)

@then('Verify Spanish language is present')
def verify_spanish_language(context):
    context.app.header.verify_spanish_language()
