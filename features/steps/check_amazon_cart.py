from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify cart is empty')
def verify_cart_empty(context):
    actually_number = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert actually_number == '0', f'Cart is not empty, there is {actually_number} in your cart'

