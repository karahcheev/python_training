from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from contact import Contact


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:444/addressbook")

    def login(self, username="admin", password="secret"):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        wd = self.wd
        """fill group form"""
        self.open_group_page()
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
        """return to group page"""
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()

    def set_info(self, form_name, info):
        self.wd.find_element_by_name(form_name).click()
        self.wd.find_element_by_name(form_name).clear()
        self.wd.find_element_by_name(form_name).send_keys(info)

    def set_contact(self, Contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
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
        self.set_days()
        self.submit_contact()
        self.return_home_page()

    def set_days(self):
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()
