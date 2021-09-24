from selenium.webdriver.common.by import By

#find page elements from Amazon sign in

#amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#continue button
driver.find_element(By.ID, 'continue')

#need help link
driver.find_element(By.XPATH, "//a[@href='javascript:void(0)' and @data-action='a-expander-toggle']")

#forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#other issues with sign in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

#conditions of us link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[text()='Conditions of Use']")


#privacy notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href,'ap_signin_notification_privacy_notice')]")

