# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    contact = Contact(firstname="firs3", lastname="last4")
    old_contacts = app.contact.get_contact_list()
    print(sorted(old_contacts, key=Contact.id_or_max))
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print("OLD CONTACT", sorted(old_contacts, key=Contact.id_or_max))
    XXXX
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



    contacts = app.contact.get_contact_list()
    print(contacts)


    old_groups = app.group.get_group_list()
    group = Group(name="group name", header="group header", footer="group footer")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
