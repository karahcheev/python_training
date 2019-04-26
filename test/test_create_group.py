# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group name", header="group header", footer="group footer")
    print(old_groups)
    app.group.create(group)
    new_groups = app.group.get_group_list()
    print(new_groups)
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    print(old_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     app.group.create(Group(name="", header="", footer=""))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
