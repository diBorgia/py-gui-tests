from pywinauto.application import Application as Winapplication
from fixture.group import GroupHelper

class Application:

    def __init__(self,target):#путь к исполн файлу
        # при помощи какой техн нужно управлять тестируемым приложением
        self.application = Winapplication(backend="win32").start(target)
        #по умолч win32
        self.main_window=self.application.window(title="Free Address Book")
        self.main_window.wait("visible") #ожидание пока не появится
        self.groups = GroupHelper(self)

    def destroy(self):
        self.application.window(title="Free Address Book").close() #тайтл в заголовке откр окна