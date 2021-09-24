from selenium.webdriver.common.by import By

#find page elements from Amazon registration

#amazon logo
driver.find_element(By.ID, 'authportal-main-section')

#creat account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#name input field
driver.find_element(By.ID, 'ap_customer_name')

#email input field
driver.find_element(By.ID, 'ap_email')

#password input field
driver.find_element(By.ID, 'ap_password')

#re-enter password input field
driver.find_element(By.ID, 'ap_password_check')

#creat account button
driver.find_element(By.ID, 'continue')

#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

#privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#sign-in link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?']")
