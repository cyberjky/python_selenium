# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


import unittest, time, re
import requests

class FindElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.pairwise.org/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_find_all_links(self):
        driver = self.driver
        driver.get(self.base_url)

        alllinks = list(driver.find_elements_by_tag_name("a"))
        cleanlinks = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        for links in alllinks:
            temp = str(links.get_attribute("href"))
            if temp.startswith("http") is True:
                cleanlinks.append(temp)

        for links in cleanlinks:
            print(links)

        for url_item in cleanlinks:
            req = requests.get(url_item, headers=headers, timeout=20)
            if req.status_code < 400:
                print("%d OK : %s" % (req.status_code, url_item))
            else:
                print("%d Error : %s" % (req.status_code, url_item))

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

