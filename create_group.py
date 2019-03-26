# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(Group(name="group name", header="group header", footer="group footer"))
    app.logout()


def test_add_empty_group(app):
    app.login()
    app.fill_group_form(Group(name="", header="", footer=""))
    app.logout()
