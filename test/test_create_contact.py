# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 10),
            address=random_string("adress1", 30),
            homephone=random_string("111", 11),
            mobilephone=random_string("222", 11),
            workphone=random_string("333", 11),
            email=random_string("email1", 15),
            email3=random_string("email3", 10),
            address2=random_string("adress2", 25),
            secondaryphone=random_string("444", 15)
    )
    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

