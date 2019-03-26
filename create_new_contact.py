# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.set_contact(Contact(firstname="asdfga", middlename="adsfasdf", lastname="adads", nickname="adfsasdf",
                            title="sfasdf", company="asdfaf", address="adsfadsf", home="adfasfd", mobile="asdfasdf",
                            work="asdfaf", fax="adffda", email="asdf", homepage="asdf", address2="asd", phone2="asdf",
                            note="asdf")
                    )
    app.logout()
