# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_contact_form(Group(name="group name", header="group header", footer="group footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_contact_form(Group(name="", header="", footer=""))
    app.session.logout()