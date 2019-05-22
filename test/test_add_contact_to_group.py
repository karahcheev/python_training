import random
from fixture.orm import ORMFixture
from model.contact import Contact

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="adding to group"))
    random_group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    print("random_group = ", random_group.name)
    print("contact = ", contact.id)
    app.contact.add_contact_to_group_by_id(contact.id, random_group.name)
    contact_in_group = orm.get_contacts_in_group(random_group)
    assert contact in contact_in_group
