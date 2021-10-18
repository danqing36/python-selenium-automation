from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count')
    CART_INFO = (By.CSS_SELECTOR, 'h2')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)


    def click_search(self):
        self.click(*self.SEARCH_ICON)


    def click_orders(self):
        self.click(*self.ORDERS)


    def click_cart(self):
        self.click(*self.CART)


    def verify_shopping_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.CART_INFO)


    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)