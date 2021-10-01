from selenium.webdriver.common.by import By
from behave import given, when, then

COLORS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given('Open Amazon Product {product_info} Page')
def open_amazon_product_detail_page(context, product_info):
    context.driver.get(f'https://www.amazon.com/dp/{product_info}/')


@then('verify color can be clicked')
def verify_product_colors(context):
    expected_color = ['Black', 'Mocha']
    colors = context.driver.find_elements(*COLORS)
    for color in range(len(colors)):
        colors[color].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_color[color], f'current color is {current_color} not match {expected_color[color]}'
