from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href*='privacy']")
PRIVACY_TEXT = (By.XPATH, "//h1[text()='Amazon.com Privacy Notice']")

@given('Open amazon help and customer service page')
def open_help_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer'
                       +'/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)


@then('Verify Amazon Privacy Notice page opened')
def privacy_page_opened(context):
    assert context.driver.find_element(*PRIVACY_TEXT)


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('Switch back to original window')
def switch_to_old_window(context):
    context.driver.switch_to_window(context.original_window)