# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import  Group

class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        """open home page"""
        wd.get("http://localhost:444/addressbook/index.php")

    def login(self, wd, username="admin", password="secret"):
        """login"""
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, wd, group):
        """fill group form"""
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        """submit creation"""
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
                wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.fill_group_form(wd, Group(name="group name", header="group header", footer="group footer"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_epty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_group_page(wd)
        self.fill_group_form(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()