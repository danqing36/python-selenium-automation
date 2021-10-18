from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
    FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)


    def find_first_product(self):
        self.wait_for_element_click(*self.FIRST_PRODUCT)