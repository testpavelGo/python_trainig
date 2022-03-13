# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_login_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    # open new contact page
    def open_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, wd):
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

    def open_main_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_contact_page(wd)
        self.create_contact(wd)
        self.open_main_page(wd)
        self.login(wd)





    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
