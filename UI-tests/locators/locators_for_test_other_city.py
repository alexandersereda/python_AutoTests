from selenium.webdriver.common.by import By

class Locators:

    SELECT_OTHER_CITY = (By.XPATH, '//div[@class="main-nav__city"]//button[contains(text()," Нет, выбрать город ")]')
    SELECT_NSK_CITY = (By.XPATH, '//div[@class="main-nav__city"]//a[@data-href="https://nsk.dostaevsky.ru"]')
    PHONE_NSK = (By.XPATH, '//a[@href="tel:+7383207-87-78"]')
