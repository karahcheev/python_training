# import re
# from random import randrange
from model.contact import Contact


def test_contact_info(app, db, check_ui):
    contact = Contact(firstname="firstname", lastname="lastname", address="City\nStreet\nHouse",
                      email="email@mailbox.test", email2="email2@mailbox.test",
                      homephone="+71112223344", workphone="(495)5553535", mobilephone="555 35 35")
    if app.contact.count() == 0:
        app.contact.create(contact)

    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)




# def merge_phones_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
#
#
# def merge_emails_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             filter(lambda x: x is not None,
#                                    map(lambda x: clear(x),
#                                            [contact.email, contact.email2, contact.email3]))))
#
#
# def clear(s):
#     return re.sub("[() -]", "", s)
