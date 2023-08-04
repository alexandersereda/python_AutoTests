import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml


def read_config():
    with open("conf.yaml", "r") as file:
        return yaml.safe_load(file)

def test_check_elements_presence(driver):
    config = read_config()
    baseurl = config["baseurl"]["BASEURL"]
    
    # Открываем страницу для теста
    driver.get(baseurl)

    # Находим элементы с помощью XPath и проверяем их наличие
    element1_present = len(driver.find_elements(By.XPATH, "//a[@class='main-nav__link main-nav__link_promo' and @href='/promo']")) > 0
    element2_present = len(driver.find_elements(By.XPATH, "//div[@class='title-secondary']")) > 0
    element3_present = len(driver.find_elements(By.XPATH, "//a[@class='footer-link__link' and @href='/license-agreement']")) > 0

    # Проверяем результаты теста
    assert element1_present, "Элемент 'Акции' не найден на странице."
    assert element2_present, "Элемент 'Популярное' не найден на странице."
    assert element3_present, "Элемент 'Лицензионное соглашение' не найден на странице."

    # Подсчитываем количество элементов <li class="main-nav__item">
    main_nav_list = driver.find_element(By.XPATH, "//ul[@class='main-nav__list']")
    li_elements = main_nav_list.find_elements(By.XPATH, ".//li[@class='main-nav__item']")
    li_count = len(li_elements)

    print(f"Number of <li class='main-nav__item'> elements: {li_count}")
    
    # Проверяем наличие элемента "Избранное", если пользователь авторизован
    try:
        favorite_element_present = len(driver.find_elements(By.XPATH, "//div[@class='main-nav__fav main-nav__link main-nav__link_fav' and @href='/favorites']")) > 0
    except:
        favorite_element_present = False

    if favorite_element_present:
        print("Элемент 'Избранное' присутствует.")
    else:
        print("Элемент 'Избранное' отсутствует.")
