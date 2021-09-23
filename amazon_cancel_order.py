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
elem.send_keys('Cancel Order')
elem.send_keys(Keys.RETURN)

assert "Cancel Items or Orders" in driver.page_source, f'Cancel Items or Orders text not present'

driver.close()


