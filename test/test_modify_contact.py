from model.contact import Contact


def test_modify_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="new firstname"))
    app.session.logout()
