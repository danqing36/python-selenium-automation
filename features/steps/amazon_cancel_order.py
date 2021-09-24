from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input {search_word} into search field and enter')
def search_in_the_field(context, search_word):
    context.driver.find_element(By.ID,'helpsearch').send_keys(search_word, Keys.ENTER)

@then('Verify cancel order are shown')
def verify_tests_results(context):
    actual_text = context.driver.find_element(By.XPATH,"//div[@class='help-content']/h1").text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'




