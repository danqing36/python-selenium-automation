from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')


    def get_product_name(self) -> str:
        product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'product name is {product_name}')
        return product_name


    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_CART_BUTTON)