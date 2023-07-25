from selenium.webdriver.common.by import By

class Locators:
    SEARCH_FIELD = (By.XPATH, '//*[@id="APjFqb"]')
    RESULT_BLOCK = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite')
