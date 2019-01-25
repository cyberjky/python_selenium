# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Actions


class MakeAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        print(type(cls.driver))
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/")
        cls.verificationErrors = []
        cls.accept_next_alert = True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.assertEqual([], cls.verificationErrors)

    def test_1_login(cls):
        driver = cls.driver
        Actions.login(driver)

    def test_2_make_appointment(cls):

        driver = cls.driver
        # Actions.login(driver)
        # driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.find_element_by_id("combo_facility").click()
        Select(driver.find_element_by_id("combo_facility")).select_by_visible_text("Seoul CURA Healthcare Center")
        driver.find_element_by_id("chk_hospotal_readmission").click()
        driver.find_element_by_id("radio_program_medicaid").click()
        driver.find_element_by_id("txt_visit_date").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::td[38]").click()
        driver.find_element_by_id("txt_comment").click()
        driver.find_element_by_id("txt_comment").clear()
        driver.find_element_by_id("txt_comment").send_keys("Please make appointment as soon as possible.")
        driver.find_element_by_id("btn-book-appointment").click()
    
    def is_element_present(cls, how, what):
        try: cls.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(cls):
        try: cls.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(cls):
        try:
            alert = cls.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
