from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TITLE = (By.CSS_SELECTOR, "div.a-section h1")
BOX_NUMBER = (By.CSS_SELECTOR, "div.a-box-inner")
SEARCH_LABEL = (By.ID, "help-search-label")
SEARCH_BOX = (By.ID, "helpsearch")
TOPIC_LINKS = (By.CSS_SELECTOR, "div.csg-hover-box-content")

@given('Open amazon customer service page')
def open_amazon_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify page title {title}')
def verify_page_title(context, title):
    actual_title = context.driver.find_element(*TITLE).text
    assert actual_title == title, f'expected title is {title}, but actual title is {actual_title}'


@then('Verify {box_number} something you can do boxes')
def verify_box_numbers(context, box_number):
    actual_box_numbers = len(context.driver.find_elements(*BOX_NUMBER))
    assert actual_box_numbers == int(box_number), f'expected box number is {box_number}, but got {actual_box_numbers} boxes'


@then('Verify search box')
def verify_search_help(context):
    actual_search_label = context.driver.find_element(*SEARCH_LABEL).text
    #Assert.assertTrue(actual_search_label.contains('Search the help library'))
    actual_search_box = context.driver.find_element(*SEARCH_BOX)
    #print(actual_search_box)


@then('Verify {topic_links} help topics')
def verify_topic_links(context, topic_links):
    actual_topic_links = len(context.driver.find_elements(*TOPIC_LINKS))
    assert actual_topic_links == int(topic_links), f'actual topic links is {actual_topic_links}, expected {topic_links} links'