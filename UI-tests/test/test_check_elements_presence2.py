import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

# @pytest.fixture(scope="session")
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def test_check_element1_presence(driver, baseurl):
    driver.get(baseurl)
    element1_present = len(driver.find_elements(By.XPATH, "//a[@class='main-nav__link main-nav__link_promo' and @href='/promo']")) > 0
    assert element1_present, "Элемент 'Акции' не найден на странице."

def test_check_element2_presence(driver, baseurl):
    driver.get(baseurl)
    element2_present = len(driver.find_elements(By.XPATH, "//div[@class='title-secondary']")) > 0
    assert element2_present, "Элемент 'Популярное' не найден на странице."

def test_check_element3_presence(driver, baseurl):
    driver.get(baseurl)
    element3_present = len(driver.find_elements(By.XPATH, "//a[@class='footer-link__link' and @href='/license-agreement']")) > 0
    assert element3_present, "Элемент 'Лицензионное соглашение' не найден на странице."

def test_count_li_elements(driver, baseurl):
    driver.get(baseurl)
    main_nav_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@class='main-nav__list']"))
    )
    li_elements = main_nav_list.find_elements(By.XPATH, ".//li[@class='main-nav__item']")
    li_count = len(li_elements)
    assert li_count > 0, "No <li class='main-nav__item'> elements found on the page."
    print(f"Number of <li class='main-nav__item'> elements: {li_count}")

def test_check_favorite_element(driver, baseurl):
    driver.get(baseurl)
    try:
        favorite_element_present = len(driver.find_elements(By.XPATH, "//div[@class='main-nav__fav main-nav__link main-nav__link_fav' and @href='/favorites']")) > 0
    except:
        favorite_element_present = False

    if favorite_element_present:
        print("Element 'Избранное' is present.")
    else:
        print("Element 'Избранное' is not present.")
