from pages.base_page import Page

class SignIn(Page):
    PAGENAME = "signin"

    def verify_signin_page_open(self):
        self.verify_url_contains_query(self.PAGENAME)
