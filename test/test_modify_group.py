from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    group = Group(name="before deleting")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    mod_group = random.choice(old_groups)
    group.id = mod_group.id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(mod_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
