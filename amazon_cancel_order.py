from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/fq/Documents/careerist/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

elem = driver.find_element(By.ID,'helpsearch')

elem.clear()
elem.send_keys('Cancel Order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH,"//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'
assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
assert "Cancel Items or Orders" in driver.page_source, f'Cancel Items or Orders text not present'

driver.close()


