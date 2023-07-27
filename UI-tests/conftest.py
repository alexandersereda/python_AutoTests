from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import yaml


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager(
        url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json", 
        driver_version = "115.0.5790.3").install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def conf():
    with open('conf.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


@pytest.fixture()
def baseurl(conf):
    return conf['baseurl']['BASEURL']
