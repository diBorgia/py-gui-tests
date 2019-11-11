from pywinauto.application import Application
import time

class GroupHelper:

    def __init__(self,app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        #в инспекторе ищем AutomationID
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        #работает только если вложенных групп нет
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self,name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        #нет свойства AutomationID,но есть ClassName
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        #энтер, чтоб завершить ввод
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def modify_group_by_id(self,data_old,data_new):
        self.open_group_editor()
        #https: // pywinauto.readthedocs.io / en / latest / controls_overview.html  # treeview
        #[u'Connection', u'Data']
        self.group_editor.TreeView.GetItem([u'\\Contact groups',u'\\%s'%data_old]).Click()
        #input = self.group_editor.window(runtime_id="[42.462370.2.232091824]").click()
        self.group_editor.window(auto_id="uxEditAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(data_new)
        #энтер, чтоб завершить ввод
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group(self,name):
        self.open_group_editor()
        input = self.group_editor.TreeView.GetItem([u'\\Contact groups',u'\\%s'%name]).Click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        #нет свойства AutomationID,но есть ClassName
        self.group_delete = self.app.application.window(title="Delete group")
        self.group_delete.wait("visible")
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

