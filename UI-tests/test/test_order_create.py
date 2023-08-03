from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
from locators.locators_for_test_order_create import Locators as Locators
import time


class TestOrderCreate():

    def test_order_georgia(self, driver_authorized, baseurl):

        # Открываем браузер с авторизированным пользователем
        page = BasePage(driver_authorized, baseurl)
        page.open()
        page.element_is_visible(Locators.DOSTA_LOGO)
        assert "Алексей" == page.element_is_visible(Locators.PROFILE_NAME).text

        # Открываем меню "Грузия"
        menu_card = page.element_is_visible(Locators.GEORGIA_MENU_CARD)
        menu_card.click()
        assert "Грузия" == page.element_is_visible(Locators.TITLE_GEORGIA).text

        # Дабавляем товары в корзину
        add_harcho = page.element_is_visible(Locators.BUTTON_HARCHO)
        add_harcho.click()
        add_hachapuri_boat = page.element_is_visible(Locators.BUTTON_HACHAPURI_BOAT)
        add_hachapuri_boat.click()
        add_hachapuri_boat = page.element_is_visible(Locators.ADD_ONE_MORE_HACHAPURI_BOAT)
        add_hachapuri_boat.click()
        assert "3" == page.element_is_visible(Locators.AMOUNT_OF_GOODS).text

        # Открываем корзину
        open_cart = page.element_is_visible(Locators.OPEN_CART)
        open_cart.click()
        assert "Корзина" == page.element_is_visible(Locators.CART).text
        assert "Харчо" == page.element_is_visible(Locators.CART_HARCHO).text
        assert "Хачапури лодочка" == page.element_is_visible(Locators.CART_HACHAPURI).text

        # Переходим на страницу оформления заказа
        button_continue = page.element_is_visible(Locators.BUTTON_CONTINUE)
        button_continue.click()
        assert 'Оформление заказа' == page.element_is_visible(Locators.ORDERING).text
        assert '+7 921 362-92-66' == page.element_is_visible(Locators.CLIENT_PHONE).text

        # Выбираем Адрес, Дату, Время и Способ оплаты заказа
        address_select = page.element_is_visible(Locators.ADDRESS_SELECT)
        address_select.click()
        delayed_delivery = page.element_is_visible(Locators.DELAYED_DELIVERY)
        delayed_delivery.click()
        main_page = ActionChains(driver_authorized)
        delivery_day = page.element_is_visible(Locators.SELECT_DAY_DELIVERY)
        delivery_day.click()
        select_day = page.element_is_visible(Locators.SELECT_TOMORROW)
        main_page.move_to_element(select_day).click().perform()
        delivery_time = page.element_is_visible(Locators.SELECT_TIME_DELIVERY)
        delivery_time.click()
        select_time = page.element_is_visible(Locators.SELECT_TIME)
        main_page.move_to_element(select_time).click().perform()
        payment_method = page.element_is_visible(Locators.PAYMENT_METHOD)
        payment_method.click()
