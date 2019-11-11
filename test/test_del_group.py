def test_del_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    app.groups.delete_group("my group")
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove("my group")
    assert sorted(old_list) == sorted(new_list)