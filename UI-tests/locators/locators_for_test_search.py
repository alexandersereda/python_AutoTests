from selenium.webdriver.common.by import By

class Locators:
    SEARCH_FIELD = (By.XPATH, '//textarea[@type="search"]')
    RESULT_BLOCK = (By.XPATH, '//div/cite[contains(text(),"dostaevsky.ru")]')
   