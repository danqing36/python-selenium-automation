from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart')
    CART_INFO = (By.CSS_SELECTOR, 'h2')


    def open_main_page(self):
        self.open_page()


    def click_orders(self):
        self.click(*self.ORDERS)


    def click_cart(self):
        self.click(*self.CART)


    def verify_shopping_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.CART_INFO)