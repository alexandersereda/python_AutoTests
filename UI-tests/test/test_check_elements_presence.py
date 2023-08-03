import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Инициализация драйвера браузера перед каждым тестом
    driver = webdriver.Chrome()  # Предполагается, что у вас установлен Chrome WebDriver
    yield driver
    # Закрытие браузера после каждого теста
    driver.quit()

def test_check_elements_presence(driver):
    # Открываем страницу для теста (замените URL на свой)
    driver.get("https://dostaevsky.ru/")

    # Находим элементы с помощью XPath и проверяем их наличие
    element1_present = len(driver.find_elements(By.XPATH, "//a[@class='main-nav__link main-nav__link_promo' and @href='/promo']")) > 0
    element2_present = len(driver.find_elements(By.XPATH, "//a[@class='title-secondary']")) > 0
    element3_present = len(driver.find_elements(By.XPATH, "//a[@class='footer-link__link' and @href='/license-agreement']")) > 0

    # Проверяем результаты теста
    assert element1_present, "Element 1 not found on the page."
    assert element2_present, "Element 2 not found on the page."
