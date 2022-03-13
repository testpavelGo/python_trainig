# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("FFname")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Mm name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Ll name")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Nn")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("comp")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("addr 1")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+73258")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+7123456789")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@test.ei")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("May")
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1999")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("8888")
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("test_group")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("addr 2")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("homie")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(u"123\n%^&\nйцук\nqwert")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True



    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
