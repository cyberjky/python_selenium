# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class MakeAppointment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_make_appointment(self):
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.find_element_by_id("btn-make-appointment").click()
        driver.find_element_by_id("txt-username").click()
        driver.find_element_by_id("txt-username").clear()
        driver.find_element_by_id("txt-username").send_keys("John Doe")
        driver.find_element_by_id("txt-password").clear()
        driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element_by_id("btn-login").click()
        driver.find_element_by_id("combo_facility").click()
        Select(driver.find_element_by_id("combo_facility")).select_by_visible_text("Seoul CURA Healthcare Center")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Facility'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Healthcare Program'])[1]/following::label[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Visit Date (Required)'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::td[38]").click()
        driver.find_element_by_id("txt_comment").click()
        driver.find_element_by_id("txt_comment").clear()
        driver.find_element_by_id("txt_comment").send_keys("Please make appointment as soon as possible.")
        driver.find_element_by_id("btn-book-appointment").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

