import re
from random import randrange
from model.contact import Contact


def test_contact_info(app):
    contact = Contact(firstname="firstname", lastname="lastname", address="City\nStreet\nHouse",
                      email="email@mailbox.test", email2="email2@mailbox.test",
                      homephone="+71112223344", workphone="(495)5553535", mobilephone="555 35 35")
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   map(lambda x: clear(x),
                                           [contact.email, contact.email2, contact.email3]))))


def clear(s):
    return re.sub("[() -]", "", s)
