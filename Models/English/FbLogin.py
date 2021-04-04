from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.Locators import *

import HtmlTestRunner
import time
import unittest


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_FBLogin(self):
        try:
            self.driver.get("https://www.ounass.ae/")
            print("Shift to div")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "wzrk-cancel"))
            )
            dialog_box_cancel = self.driver.find_element_by_id("wzrk-cancel")
            dialog_box_cancel.click()
            account_main_label = self.driver.find_element_by_css_selector(".Popup-iconText")
            account_main_label.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "SignInThirdpartyButtons-facebookButton"))
            )
            account_login_fb = self.driver.find_element_by_class_name("SignInThirdpartyButtons-facebookButton")
            account_login_fb.click()
            prev_url = self.driver.current_url
            print(prev_url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            usr_name = self.driver.find_element_by_css_selector("#email")
            pwd = self.driver.find_element_by_css_selector("#pass")
            fb_login_btn = self.driver.find_element_by_css_selector("#loginbutton")
            usr_name.send_keys("samad@werplay.com")
            pwd.send_keys("werplayru55")
            fb_login_btn.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".Popup-iconText")))
            account_main_label_loggedin = ElemLocators.by_css_containing_text(self.driver,".Popup-iconText","Account")
            account_main_label_loggedin[0].click()

        except Exception as ex:
            print(ex)
            self.driver.close()
            self.driver.quit()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Cycle Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports"))
