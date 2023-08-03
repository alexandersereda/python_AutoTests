from base_page import BasePage
import time
import pickle


class TestGetCookies():

    def test_get_cookies_by_authorization(self, driver, baseurl):
        page = BasePage(driver, baseurl)
        page.open()
        time.sleep(30)

        pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
        