# -*- coding: utf-8 -*-

def login(driver):
    driver.find_element_by_id("btn-make-appointment").click()
    driver.find_element_by_id("txt-username").click()
    driver.find_element_by_id("txt-username").clear()
    driver.find_element_by_id("txt-username").send_keys("John Doe")
    driver.find_element_by_id("txt-password").clear()
    driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element_by_id("btn-login").click()

