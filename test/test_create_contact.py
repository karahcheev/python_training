# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    contact = Contact(firstname="firstname4", lastname="lastname4")
    old_contacts = app.contact.get_contact_list()
    print('\nOLD CONTACTS', sorted(old_contacts, key=Contact.id_or_max))
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print('\nNEW CONTACTS', sorted(new_contacts, key=Contact.id_or_max))
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print("\nADD CONTACTS", sorted(old_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

