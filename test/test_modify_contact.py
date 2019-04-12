from model.contact import Contact


def test_modify_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="before deleting"))
    app.contact.modify_first_contact(Contact(firstname="new firstname"))

