from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import yaml
import pickle


@pytest.fixture(scope="session")
def driver():
    driver_service = Service(ChromeDriverManager(
        url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json", 
        driver_version = "115.0.5790.3").install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver_authorized():
    driver_service = Service(ChromeDriverManager(
        url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json", 
        driver_version = "115.0.5790.3").install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://dostaevsky.ru")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.save_screenshot("screenshot.png")
    driver.quit()


@pytest.fixture(scope="session")
def conf():
    with open('conf.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


@pytest.fixture(scope="session")
def baseurl(conf):
    return conf['baseurl']['BASEURL']


@pytest.fixture(scope="session")
def baseurl_ordering(conf):
    return conf['baseurl']['BASEURL_ORDERING']


@pytest.fixture(scope="session")
def googleurl(conf):
    return conf['baseurl']['GURL']
