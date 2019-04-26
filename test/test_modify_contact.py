from model.contact import Contact


def test_modify_name(app):
    contact = Contact(firstname="modifyadf", lastname="asdfasdf")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    print('\n', sorted(old_contacts, key=Contact.id_or_max))
    app.contact.modify_first_contact(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    print('\n', sorted(new_contacts, key=Contact.id_or_max))
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    print(sorted(old_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
