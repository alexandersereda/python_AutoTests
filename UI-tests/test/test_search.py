from selenium.webdriver import Keys
from base_page import BasePage
from locators.locators_for_test_search import Locators as Locators


class TestPage():

    def test_dosta_search(self, driver, baseurl):
        page = BasePage(driver, baseurl)
        page.open()
        searching_text = 'Достаевский'
        search = page.element_is_visible(Locators.SEARCH_FIELD)
        search.send_keys(searching_text)
        search.send_keys(Keys.RETURN)
        result = page.element_is_visible(Locators.RESULT_BLOCK)
        assert "https://dostaevsky.ru" == result.text
