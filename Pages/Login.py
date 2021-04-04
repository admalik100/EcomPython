from Pages.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

        cred_usrname = "samad@werplay.com"
        cred_pwrd = "werplayru55"
        dialog_box_cancel = driver.find_element_by_id("wzrk-cancel")
        account_main_label = self.driver.find_element_by_css_selector(".Popup-iconText")
        account_login_fb = self.driver.find_element_by_class_name("SignInThirdpartyButtons-facebookButton")
        usr_name = self.driver.find_element_by_css_selector("#email")
        pwd = self.driver.find_element_by_css_selector("#pass")
        fb_login_btn = self.driver.find_element_by_css_selector("#loginbutton")
        account_main_label_loggedin = ElemLocators.by_css_containing_text(self.driver, ".Popup-iconText",
                                                                               "Account")

