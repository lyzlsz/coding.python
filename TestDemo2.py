# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestDemo2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.2345.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_demo2(self):
        driver = self.driver
        driver.get(self.base_url + "/tg36985.htm")
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
        driver.find_element_by_id("QtQYS1564839922408").click()
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
        driver.find_element_by_id("QtQYS1564839922408").clear()
        driver.find_element_by_id("QtQYS1564839922408").send_keys(u"自动化测试")
        driver.find_element_by_id("j_search_sbm").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
        driver.find_element_by_css_selector("a.mod-arrow.mod-arrow-next").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
