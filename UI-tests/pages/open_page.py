from selenium.webdriver import Keys
from locators.locators import Locators as Locators
from pages.base_page import BasePage


class OpenPage(BasePage):
    
    def fill_and_submit(self):
        search_field = 'Достаевский'
        search = self.element_is_visible(Locators.SEARCH_FIELD)
        search.send_keys(search_field)
        search.send_keys(Keys.RETURN)
       
    def check_result(self):
        result_block = self.element_is_visible(Locators.RESULT_BLOCK)
        result_block = result_block.text
        assert "https://dostaevsky.ru" == result_block
