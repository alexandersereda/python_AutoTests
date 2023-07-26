import time
from pages.open_page import OpenPage
from locators.locators import Locators as Locators


class TestPage:

    def test_search(self, driver):
        searching_page = OpenPage(driver, 'https://www.google.com/')
        searching_page.open()
        searching_page.fill_and_submit()
        result = searching_page.check_result()
        