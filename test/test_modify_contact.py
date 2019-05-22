from model.contact import Contact
import random


def test_modify_name(app, db, check_ui):
    contact = Contact(firstname="modifyadf", lastname="asdfasdf")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    mod_contact = random.choice(old_contacts)
    contact.id = mod_contact.id
    app.contact.modify_contact_by_id(contact.id, contact)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    old_contacts.remove(mod_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
