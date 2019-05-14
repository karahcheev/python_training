# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    contact = Contact(firstname="firstname3", lastname="lastname3", address="City3\nStreet3\nHouse3",
                      email="email@mailbox.test", email2="email2@mailbox.test",
                      homephone="+71112223344", workphone="(495)5553535", mobilephone="555 35 35")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

