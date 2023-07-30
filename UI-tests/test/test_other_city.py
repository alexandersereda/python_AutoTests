from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
from locators.locators_for_test_other_city import Locators as Locators


class TestOtherCitySelect():

    def test_other_city_select(self, driver, baseurl):
        page = BasePage(driver, baseurl)
        page.open()
        main_page = ActionChains(driver)
        search = page.element_is_visible(Locators.SELECT_OTHER_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.SELECT_NSK_CITY)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_NSK)
        assert "8 (383) 207-87-78" == result.text
