from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignIn
from pages.search_results_page import SearchResults
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in = SignIn(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

