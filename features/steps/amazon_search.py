from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_ORDERS = (By.ID, 'nav-orders')

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click on orders icon')
def click_orders_icon(context):
    context.app.header.click_orders()

@when('Hover over language options')
def hover_over_language_options(context):
    context.app.header.hover_over_language_options()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()


@then('signin page is opened')
def verify_found_results_text(context):
    context.app.sign_in.verify_signin_page_open()

@then('verify {info} text present')
def verify_shopping_cart_empty(context, info):
    context.app.header.verify_shopping_cart_empty(info)

@then('Verify correct options present')
def verify_correct_options_present(context):
    context.app.header.verify_correct_options_present()


@when('Select department by alias {department_name}')
def select_department(context, department_name):
    context.app.header.select_department(department_name)


@then('Verify {department_name} department is selected')
def verify_department_selected(context, department_name):
    context.app.search_results_page.verify_department_selected(department_name)