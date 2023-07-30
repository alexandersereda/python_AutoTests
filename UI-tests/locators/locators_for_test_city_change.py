from selenium.webdriver.common.by import By

class Locators:
    
    MAIN_CITY_CONFIRM = (By.XPATH, '//div[@class="main-nav__city"]//button[contains(text(),"Да")]')
    SELECT_CITY = (By.XPATH, '//div[@class="main-nav__city"]')
    CITY_CONFIRM_SPB = (By.XPATH, '//a[@href="https://dostaevsky.ru/"]')
    PHONE_SPB = (By.XPATH, '//a[@href="tel:+7812777-80-08"]')
    CITY_CONFIRM_MSK = (By.XPATH, '//a[@href="https://msk.dostaevsky.ru/"]')
    PHONE_MSK = (By.XPATH, '//a[@href="tel:+7495788-78-78"]')
    CITY_CONFIRM_SOCHI = (By.XPATH, '//a[@href="https://sochi.dostaevsky.ru/"]')
    PHONE_SOCHI = (By.XPATH, '//a[@href="tel:+7862296-78-78"]')
    CITY_CONFIRM_KRD = (By.XPATH, '//a[@href="https://krd.dostaevsky.ru/"]')
    PHONE_KRD = (By.XPATH, '//a[@href="tel:+7861205-88-77"]')
    CITY_CONFIRM_NSK = (By.XPATH, '//a[@href="https://nsk.dostaevsky.ru/"]')
    PHONE_NSK = (By.XPATH, '//a[@href="tel:+7383207-87-78"]')
    