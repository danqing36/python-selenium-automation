from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class SearchResults(Page):
    SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
    FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    FIRST_DEPARTMENT = (By.CSS_SELECTOR, 'span.nav-a-content')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='s/ref=sr_hi']")
    NEW_ARRIVALS_POP = (By.XPATH, "//div[contains(@id,'nav-flyout-aj')]")

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)


    def find_first_product(self):
        self.wait_for_element_click(*self.FIRST_PRODUCT)

    def verify_department_selected(self, department_name):
        self.verify_text(department_name, *self.FIRST_DEPARTMENT)

    def hover_over_new_arrivals_option(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(5)

    def verify_new_arrivals_options(self, number):
        number_of_pop = len(self.find_elements(*self.NEW_ARRIVALS_POP))
        assert number == str(number_of_pop), f'pop up {number_of_pop} new arrivals, but expected {number} pop up'