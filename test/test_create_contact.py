# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    contact = Contact(firstname="firstname4", lastname="lastname4", address="adress1",
                      homephone="1111111", mobilephone="222222", workphone="333333",
                      email="email1", email3="email3", address2="adress2", secondaryphone="444444")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

