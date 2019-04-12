# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="asdfga", middlename="adsfasdf", lastname="adads", nickname="adfsasdf",
                                          title="sfasdf", company="asdfaf", address="adsfadsf", home="adfasfd", mobile="asdfasdf",
                                          work="asdfaf", fax="adffda", email="asdf", homepage="asdf", address2="asd", phone2="asdf",
                                          note="asdf"))