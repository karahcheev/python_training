from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="before deleting"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
