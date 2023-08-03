from selenium.webdriver.common.by import By

class Locators:

    DOSTA_LOGO = (By.XPATH, '//div[@class="header__logo"]')
    GEORGIA_MENU_CARD = (By.XPATH, '//div[@data-title="Грузия"]')
    PROFILE_NAME = (By.XPATH, '//span[@class="authorization-button__text"][text()=" Алексей "]')
    TITLE_GEORGIA = (By.XPATH, '//div[@class="title"][text()="Грузия"]')
    BUTTON_HARCHO = (By.XPATH, '//button[@data-id="eccaf0fd-8cde-442f-8231-82d31a408d01"][text()=" В корзину "]')
    BUTTON_HACHAPURI_BOAT = (By.XPATH, '//button[@data-id="13614c9b-db35-4d63-ab8f-3044a82c8b82"][text()=" В корзину "]')
    ADD_ONE_MORE_HACHAPURI_BOAT = (By.XPATH, '//button[@data-id="13614c9b-db35-4d63-ab8f-3044a82c8b82"][text()=" + "]')
    AMOUNT_OF_GOODS = (By.XPATH, '//span[@class="catalog-cart__count"][text()="3"]')
    OPEN_CART = (By.XPATH, '//button[@title="Открыть корзину"]')
    CART = (By.XPATH, '//span[text() = "Корзина"]')
    CART_HARCHO = (By.XPATH, '//p[@class="basket__product-title"][text() = "Харчо"]')
    CART_HACHAPURI = (By.XPATH, '//p[@class="basket__product-title"][text() = "Хачапури лодочка"]')
    BUTTON_CONTINUE = (By.XPATH, '//button[@type="button"][text() = "Продолжить"]')
    ORDERING = (By.XPATH, '//div[@class="title-form"][text() = "Оформление заказа"]')
    CLIENT_PHONE = (By.XPATH, '//div[@class="order-form-phone"][text() = " +7 921 362-92-66 "]')
    ADDRESS_SELECT = (By.XPATH, '//span[@class="address-name"][text() = " Тест_Платный 200 "]')
    DELAYED_DELIVERY = (By.XPATH, '//label[@for="delivery-type-delayed-field"]')
    SELECT_DAY_DELIVERY = (By.XPATH, '//select[@id="order-time-day"]')
    SELECT_TOMORROW = (By.XPATH, '//select//option[contains(text(), "Завтра,")]')
    SELECT_TIME_DELIVERY = (By.XPATH, '//select[@name="order-time-hour"]')
    SELECT_TIME = (By.XPATH, '//select//option[contains(text(), "11:00")]')
    PAYMENT_METHOD = (By.XPATH, '//label[@for="payment-type-courier-card-field"]')
    
