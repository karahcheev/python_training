# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class CreateNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit_contact(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


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

    def _open_creating_contact_page(self, driver):
        """open creating contact"""
        driver.find_element_by_link_text("add new").click()

    def _login(self, driver):
        """login"""
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def _open_homepage(self, driver):
        """open homepage"""
        driver.get("http://localhost:444/addressbook/")

    def test_create_new_contact(self):

        def set_info(form_name, info):
            wd = self.wd
            wd.find_element_by_name(form_name).click()
            wd.find_element_by_name(form_name).clear()
            wd.find_element_by_name(form_name).send_keys(info)

        wd = self.wd
        self._open_homepage(wd)
        self._login(wd)
        self._open_creating_contact_page(wd)

        """fill contact form"""
        set_info("firstname", "First name")
        set_info("middlename", "Middle name")
        set_info("lastname", "Last name")
        set_info("nickname", "nickname")
        set_info("title", "title")
        set_info("company", "company")
        set_info("address", "address")
        set_info("home", "home")
        set_info("mobile", "mobile")
        set_info("work", "work")
        set_info("fax", "fax")
        set_info("email", "email")
        set_info("homepage", "homepage")
        set_info("address2", "address2")
        set_info("phone2", "phone2")
        set_info("notes", "notes")

        self.set_days(wd)
        self.submit_contact(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
