from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LINKS = (By.XPATH, "//div[@id='zg_tabs']/ul/li")

@given('open amazon best sellers page')
def open_amazon_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify {link_number} links under menu bar')
def verify_links_under_menu_bar(context, link_number):
    actual_links_number = len(context.driver.find_elements(*LINKS))
    assert actual_links_number == int(link_number), f"There are {actual_links_number} links, but expected {link_number} links"