# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from Pages.Locators import *
# import HtmlTestRunner
# import time
# import unittest
#
#
# class GoogleSearch(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         # cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
#         cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()
#
#     def test_SearchHello(self):
#         try:
#             self.driver.get("https://www.ounass.ae/")
#             time.sleep(5)
#             print("Shift to div")
#             dialog_box_cancel = self.driver.find_element_by_id("wzrk-cancel")
#             dialog_box_cancel.click()
#             time.sleep(5)
#             account_main_label = self.driver.find_element_by_css_selector(".Popup-iconText")
#             account_main_label.click()
#             time.sleep(5)
#             account_login_fb = self.driver.find_element_by_class_name("SignInThirdpartyButtons-facebookButton")
#             account_login_fb.click()
#             time.sleep(5)
#             prev_url = self.driver.current_url
#             print(prev_url)
#
#             usr_name = self.driver.find_element_by_css_selector("#email")
#             pwd = self.driver.find_element_by_css_selector("#pass")
#             fb_login_btn = self.driver.find_element_by_css_selector("#loginbutton")
#             usr_name.send_keys("samad@werplay.com")
#             pwd.send_keys("werplayru55")
#             fb_login_btn.click()
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, ".Popup-iconText")))
#             account_main_label_loggedin = ElemLocators.by_css_containing_text(self.driver,".Popup-iconText","Account")
#             account_main_label_loggedin[0].click()
#             time.sleep(5)
#
#             # account_login = self.driver.find_element_by_link_text("customer")
#             # actions = ActionChains(self.driver)
#             # actions.move_to_element(account_main_label).perform()
#             # time.sleep(5)
#             # actions.move_to_element(account_login).click().perform()
#         except Exception as ex:
#             print(ex.with_traceback())
#
#             self.driver.close()
#             self.driver.quit()
#
#     # def test_checkout(self):
#     #     try:
#     #         self.driver.get("https://www.ounass.ae/")
#     #         time.sleep(5)
#     #         print("Shift to div")
#     #         dialog_box_cancel = self.driver.find_element_by_id("wzrk-cancel")
#     #         dialog_box_cancel.click()
#     #         time.sleep(5)
#     #         link_women = ElemLocators.by_css_containing_text(self.driver, ".Gender-title", "WOMEN")
#     #         link_women[0].click()
#     #         time.sleep(5)
#     #         product_recommended = self.driver.find_element_by_class_name("ProductSlider-title")
#     #         actions = ActionChains(self.driver)
#     #         actions.move_to_element(product_recommended).perform()
#     #         time.sleep(5)
#     #         product_recommended_shop_all = ElemLocators.by_css_containing_text(self.driver, ".ProductSlider-ctaLink",
#     #                                                                            "SHOP ALL")
#     #         product_recommended_shop_all[0].click()
#     #         time.sleep(5)
#     #         item_1 = ElemLocators.by_css_containing_text(self.driver, ".Product-name",
#     #                                                      "Botanica Smocked Yoke Mini Dress in Silk")
#     #         item_1[0].click()
#     #         size_dropdown = self.driver.find_element_by_class_name("Select-arrow-zone")
#     #         size_dropdown.click()
#     #         size_option_item = ElemLocators.by_css_containing_text(self.driver, ".Select-option-label", "2")
#     #         size_option_item[0].click()
#     #         item_addto_bag = self.driver.find_element_by_class_name("AddToBag")
#     #         item_addto_bag.click()
#     #         time.sleep(5)
#     #         bag = ElemLocators.by_css_containing_text(self.driver, ".Popup-iconText", "Bag")
#     #         bag[0].click()
#     #         checkout_items = self.driver.find_element_by_class_name("CartTotal-secureCheckout")
#     #         checkout_items.click()
#     #         element = WebDriverWait(self.driver, 10).until(
#     #             EC.presence_of_element_located((By.CSS_SELECTOR, ".ounass "))
#     #         )
#     #         customer_checkout_fname = self.driver.find_element_by_id("firstName")
#     #         customer_checkout_fname.send_keys("john")
#     #         customer_checkout_lname = self.driver.find_element_by_id("lastName")
#     #         customer_checkout_lname.send_keys("doe")
#     #         customer_checkout_email = self.driver.find_element_by_id("email")
#     #         customer_checkout_email.send_keys("example001@example.com")
#     #         customer_checkout_num = self.driver.find_element_by_id("mobileNumber")
#     #         customer_checkout_num.send_keys("67324238")
#     #         customer_checkout_emirate = ElemLocators.by_css_containing_text(self.driver,".Select-placeholder",
#     #                                                                         "Please select ...")
#     #         customer_checkout_emirate[0].click()
#     #         customer_checkout_emirate_option = self.driver.find_element_by_id("react-select-3--option-0")
#     #         customer_checkout_emirate_option.click()
#     #         customer_checkout_area = self.driver.find_element_by_class_name("pac-target-input")
#     #         customer_checkout_area.send_keys("Business Bay")
#     #         customer_checkout_st = self.driver.find_element_by_id("street")
#     #         customer_checkout_st.send_keys("st#3")
#     #         customer_checkout_apartment = self.driver.find_element_by_id("additionalInformation")
#     #         customer_checkout_apartment.send_keys("Apartment 2021")
#     #         customer_checkout_continue_btn = self.driver.find_element_by_class_name("ShippingInformationForm"
#     #                                                                                 "-submitButton")
#     #         actions = ActionChains(self.driver)
#     #         actions.move_to_element(customer_checkout_continue_btn).perform()
#     #
#     #         time.sleep(5)
#     #     except Exception as ex:
#     #         print(ex)
#     #         self.driver.close()
#     #         self.driver.quit()
#     #     finally:
#     #         print()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#         print("Test Cycle Completed")
#
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports"))
import unittest
from Models.English.FbLogin import GoogleSearch
from Models.English.CheckOut import CheckOut

tc1 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckOut)

masterTestSuite = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
