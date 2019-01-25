# -*- coding: utf-8 -*-
from selenium import webdriver
import requests

def find_elements():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    base_url = "http://www.monstertestlab.com/xe/"
    driver.get(base_url)

    alllinks = list(driver.find_elements_by_tag_name("a"))
    cleanlinks = []
    for links in alllinks:
        temp = str(links.get_attribute("href"))
        if temp.startswith("http") is True and temp.endswith(".pdf") is not True:
            cleanlinks.append(temp)

    for links in cleanlinks:
        print(links)

    for url_item in cleanlinks:
        req = requests.get(url_item, timeout=20)
        if req.status_code < 400:
            print("%d OK : %s" % (req.status_code, url_item))
        else:
            print("%d Error : %s" % (req.status_code, url_item))

    driver.quit()


find_elements()
