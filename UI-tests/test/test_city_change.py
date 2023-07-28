from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
from locators.locators_for_test_city_change import Locators as Locators


class TestCityChange():

    def test_city_change(self, driver, baseurl):
        page = BasePage(driver, baseurl)
        page.open()
        button = page.element_is_visible(Locators.MAIN_CITY_CONFIRM)
        button.click()
        result = page.element_is_visible(Locators.PHONE_SPB)
        assert "8 (812) 777-80-08" == result.text

        main_page = ActionChains(driver)
        search = page.element_is_visible(Locators.SELECT_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.CITY_CONFIRM_MSK)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_MSK)
        assert "8 (495) 788-78-78" == result.text

        search = page.element_is_visible(Locators.SELECT_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.CITY_CONFIRM_SOCHI)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_SOCHI)
        assert "8 (862) 296-78-78" == result.text

        search = page.element_is_visible(Locators.SELECT_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.CITY_CONFIRM_KRD)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_KRD)
        assert "8 (861) 205-88-77" == result.text

        search = page.element_is_visible(Locators.SELECT_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.CITY_CONFIRM_NSK)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_NSK)
        assert "8 (383) 207-87-78" == result.text

        search = page.element_is_visible(Locators.SELECT_CITY)
        main_page.move_to_element(search).perform()
        p = page.element_is_visible(Locators.CITY_CONFIRM_SPB)
        main_page.move_to_element(p).click().perform()
        result = page.element_is_visible(Locators.PHONE_SPB)
        assert "8 (812) 777-80-08" == result.text
