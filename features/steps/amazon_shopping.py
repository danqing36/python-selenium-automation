from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
PRODUCT_NAME = (By.ID, 'productTitle')
ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART_PAGE = (By.ID, 'nav-cart')
CART_NUMBER = (By.ID, 'nav-cart-count')
PRODUCT_NAME_IN_CART = (By.XPATH, "//span[@class='a-truncate-cut']")

@when('Search {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product, Keys.ENTER)


@when('Click the first product')
def find_first_product(context):
    context.driver.find_element(*FIRST_PRODUCT).click()


@when('Save the product name')
def save_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text


@when('Add the product to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()
    sleep(2)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*CART_PAGE).click()
    sleep(2)


@then('Verify cart has {number} product')
def check_product_account(context, number):
    actual_number = context.driver.find_element(*CART_NUMBER).text
    assert actual_number == number, f"Shopping cart has {actual_number} products, expect {number} products"


@then('Verify product name is correct')
def check_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME_IN_CART).text
    assert actual_name == context.product_name, f"The product in shopping cart is {actual_name}, not {context.product_name}"


