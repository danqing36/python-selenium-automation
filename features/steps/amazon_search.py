from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_ORDERS = (By.ID, 'nav-orders')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on orders icon')
def click_orders_icon(context):
    context.driver.find_element(*SEARCH_ORDERS).click()
    sleep(1)


@then('{sign_in} page is opened')
def verify_found_results_text(context, sign_in):
    assert sign_in.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"