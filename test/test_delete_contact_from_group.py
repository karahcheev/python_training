import random
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="adding to group"))
    if len(db.get_group_list()) == 0:
        group = Group(name="name1", header="header1", footer="footer1")
        app.group.create(group)

    random_group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    print("Contact ", contact.firstname, contact.lastname, "added to group ", random_group.name)
    app.contact.add_contact_to_group_by_id(contact.id, random_group.name)
    contact_in_group = orm.get_contacts_in_group(random_group)
    assert contact in contact_in_group
    app.contact.delete_contact_from_group_by_name(contact.id, random_group.name)
    assert contact not in contact_in_group
