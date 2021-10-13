from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_ORDERS = (By.ID, 'nav-orders')

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click on orders icon')
def click_orders_icon(context):
    context.app.main_page.click_orders()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.main_page.click_cart()


@then('signin page is opened')
def verify_found_results_text(context):
    context.app.sign_in.verify_signin_page_open()

@then('verify {info} text present')
def verify_shopping_cart_empty(context, info):
    context.app.main_page.verify_shopping_cart_empty(info)

