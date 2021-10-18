from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep



@when('Input {product} into amazon search')
def input_into_amazon_search(context, product):
    context.app.header.input_search(product)


@when('Click on amazon search icon')
def click_amazon_search_button(context):
    context.app.header.click_search()


@when('Click the first product')
def find_first_product(context):
    context.app.search_results_page.find_first_product()


@when('Store the product name')
def store_product_name(context):
    context.product_name = context.app.product_page.get_product_name()


@when('Click on Add to cart button')
def add_product_to_cart(context):
    context.app.product_page.click_add_to_cart()
    sleep(4)

@when('Open cart page')
def open_cart_page(context):
    context.app.header.click_cart()

@then('Verify cart has correct product name')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(context.product_name)


@then('Verify cart has {number} product')
def verify_cart_count(context, number):
    print(type(number))
    context.app.header.verify_cart_count(number)
