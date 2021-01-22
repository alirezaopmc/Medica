from uuid.uuid import UUID
from db.dbx import DBX
from prod.prod import Product



class Medica:
    """
    Application command line is handled by this class.
    """
    def __init__(self, uuid_length: int):
        """

        :param uuid_length:
        """
        self.db = None
        self.running = None
        self.menu = None
        self.uuid_tool = None
        self.uuid_length = uuid_length

    def execute(self):
        """
        execute the program for the first time and it will run
        :return:
        """
        self.start()
        while self.running:
            self.run()
        self.terminate()

    def run(self):
        self.show_menu()

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        self.uuid_tool = UUID('./uuid/salt.txt', self.uuid_length)
        self.db = DBX('./db/db.xlsx', self.uuid_tool)
        self.db.load()
        self.menu = self.menu_home

    def terminate(self):
        self.save()

    def save(self):
        self.db.save()
        pass

    # Menu Functionality
    def menu_home(self):
        print('1. List all categories')
        print('2. List all items')
        print('3. Add new items')
        print('0. Exit')

        self.get_menu()

    def menu_list_categories(self):
        self.db.show_categories(10)
        self.menu = self.menu_home

    def menu_list_items(self):
        self.db.show_items(10)
        self.menu = self.menu_home

    def menu_add_items(self):
        pass

    def show_menu(self):
        self.menu()

    def get_menu(self):
        menu_index = input("=> ")

        if menu_index == '0':
            print('Terminated')
            self.stop()
            return

        if self.menu == self.menu_home:
            if menu_index == '1':
                self.menu = self.menu_list_categories
            if menu_index == '2':
                self.menu = self.menu_list_items
            if menu_index == '3':
                self.menu = self.menu_add_items

            return

        if self.menu == self.menu_list_categories:
            self.menu = self.menu_home

            return

        if self.menu == self.menu_list_items:
            self.menu = self.menu_home

            return

        if self.menu == self.add_items:
            pass

            return
