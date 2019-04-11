from model.contact import Contact


def test_modify_name(app):
    app.contact.modify_first_contact(Contact(firstname="new firstname"))

