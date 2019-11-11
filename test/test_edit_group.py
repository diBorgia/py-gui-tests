import random

def test_edit_group(app):
    data_old = "General"
    old_list = app.groups.get_group_list()
    if (len(old_list) == 0) or not (data_old in old_list):
        app.groups.add_new_group("General")
        old_list = app.groups.get_group_list()
    data_new = "New666"
    app.groups.modify_group_by_id(data_old,data_new)
    new_list = app.groups.get_group_list()
    old_list.remove(data_old)
    old_list.append(data_new)
    assert sorted(old_list) == sorted(new_list)