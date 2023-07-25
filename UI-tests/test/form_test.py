import time
from pages.open_page import OpenPage
from locators.locators import Locators as Locators


class TestPage:

    def test_form(self, driver):
        form_page = OpenPage(driver, 'https://www.google.com/')
        form_page.open()
        form_page.fill_and_submit()
        result = form_page.check_result()
        