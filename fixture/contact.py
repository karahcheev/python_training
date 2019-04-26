from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_link_text("Last name")) > 0:
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("title", contact.title)
        # self.change_field_value("company", contact.company)
        # self.change_field_value("address", contact.address)
        # self.change_field_value("home", contact.home)
        # self.change_field_value("mobile", contact.mobile)
        # self.change_field_value("work", contact.work)
        # self.change_field_value("fax", contact.fax)
        # self.change_field_value("email", contact.email)
        # self.change_field_value("homepage", contact.homepage)
        # self.change_field_value("address2", contact.address2)
        # self.change_field_value("phone2", contact.phone2)
        # self.change_field_value("notes", contact.note)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        #self.set_days()
        self.submit_contact()
        self.app.return_home_page()
        self.contact_cache = None

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

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_list()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cell = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=cell[2].text, lastname=cell[1].text, id=id))
            return list(self.contact_cache)
