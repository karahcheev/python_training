from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def set_info(self, form_name, info):
        self.app.wd.find_element_by_name(form_name).click()
        self.app.wd.find_element_by_name(form_name).clear()
        self.app.wd.find_element_by_name(form_name).send_keys(info)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.set_info("firstname", contact.firstname)
        self.set_info("middlename", contact.middlename)
        self.set_info("lastname", contact.lastname)
        self.set_info("nickname", contact.nickname)
        self.set_info("title", contact.title)
        self.set_info("company", contact.company)
        self.set_info("address", contact.address)
        self.set_info("home", contact.home)
        self.set_info("mobile", contact.mobile)
        self.set_info("work", contact.work)
        self.set_info("fax", contact.fax)
        self.set_info("email", contact.email)
        self.set_info("homepage", contact.homepage)
        self.set_info("address2", contact.address2)
        self.set_info("phone2", contact.phone2)
        self.set_info("notes", contact.note)
        self.set_days()
        self.submit_contact()
        self.app.return_home_page()

    def set_days(self):
        wd = self.app.wd
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

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()