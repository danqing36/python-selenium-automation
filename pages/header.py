from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count')
    CART_INFO = (By.CSS_SELECTOR, 'h2')
    FLAG = (By.CSS_SELECTOR, 'span.icp-nav-link-inner')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    ENGLISH_LANG = (By.XPATH, '//header[@id="navbar-mian"]//*[contains(text(),English)]')
    DEPARTMENT = (By.ID, 'searchDropdownBox')


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)


    def click_search(self):
        self.click(*self.SEARCH_ICON)


    def hover_over_language_options(self):
        lang = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()
        sleep(5)

    def click_orders(self):
        self.click(*self.ORDERS)


    def click_cart(self):
        self.click(*self.CART)


    def verify_shopping_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.CART_INFO)


    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def verify_correct_options_present(self):
        self.wait_for_element_appear(*self.ENGLISH_LANG)
        self.find_element(*self.SPANISH_LANG)

    def select_department(self, department_name: str):
        select = Select(self.find_element(*self.DEPARTMENT))
        select.select_by_visible_text(department_name)