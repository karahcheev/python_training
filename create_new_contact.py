# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact
import time

class CreateNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    def set_info(self, form_name, info):
        self.wd.find_element_by_name(form_name).click()
        self.wd.find_element_by_name(form_name).clear()
        self.wd.find_element_by_name(form_name).send_keys(info)
    def open_homepage(self, wd):
        wd.get("http://localhost:444/addressbook/")
    def login(self, wd, username, password):
        self.set_info("user", username)
        self.set_info("pass", password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
    def open_creating_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def set_contact(self, Contact):
        self.set_info("firstname", Contact.firstname)
        self.set_info("middlename", Contact.middlename)
        self.set_info("lastname", Contact.lastname)
        self.set_info("nickname", Contact.nickname)
        self.set_info("title", Contact.title)
        self.set_info("company", Contact.company)
        self.set_info("address", Contact.address)
        self.set_info("home", Contact.home)
        self.set_info("mobile", Contact.mobile)
        self.set_info("work", Contact.work)
        self.set_info("fax", Contact.fax)
        self.set_info("email", Contact.email)
        self.set_info("homepage", Contact.homepage)
        self.set_info("address2", Contact.address2)
        self.set_info("phone2", Contact.phone2)
        self.set_info("notes", Contact.note)

    def set_days(self, wd):
        """set bday"""
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1970")
        """set aday"""
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
    def submit_contact(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()
    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_create_contact(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_creating_contact_page(wd)
        time.sleep(2)
        self.set_contact(Contact(firstname="asdfga", middlename="adsfasdf", lastname="adads", nickname="adfsasdf", title="sadfasdf", company="asdfaf", address="adsfadsf", home="adfasfd", mobile="asdfasdf", work="asdfaf", fax="adffda", email="asdf", homepage="asdf", address2="asd", phone2="asdf", note="asdf"))
        self.set_days(wd)
        self.submit_contact(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
