from openpyxl import load_workbook
from prod.prod import Product
from uuid.uuid import UUID
from datetime import datetime
from math import log
from util import console


class DBX:
    """
    Excel database is handled by this class.
    """
    def __init__(self, path: str, uuid_tool: UUID):
        """
        :param path: path to the excel file
        """
        self.path = path
        self.uuid_tool = uuid_tool
        self.wb = None
        self.ws = None
        self.products = None
        self.products_count = None
        self.cats = None
        self.uuids = None

    def load(self) -> None:
        """
        load products from excel file
        :return:
        """
        self.wb = load_workbook(self.path)
        self.ws = self.wb.active
        self.cats = set()
        self.uuids = set()
        self.products = {}
        self.products_count = 0

        items = [list(map(lambda x: x.value, row)) for row in self.ws]
        self.products_count = len(items)
        for i in range(len(items)):
            item = Product(i, items[i])
            self.products[item.uuid] = item
            self.cats.add(item.name)
        print('Excel Database has been loaded successfully')

    def add_items(self, name: str, count: int, date: str, exp: int) -> None:
        """
        add as many items
        :param name: category name
        :param count: number of items to be added
        :param date: mm/dd/yyyy format of the products date
        :param exp: number of days what the item will expire after
        :return:
        """
        console.line()
        console.header('Item insertion menu')
        self.products_count += count

        if name not in self.cats:
            self.cats.add(name)

        for i in range(count):
            uuid = self.uuid_tool.new(self.uuids)
            data = [
                uuid,
                name,
                date,
                exp
            ]
            item = Product(self.products_count, data)
            self.products[uuid] = item

        console.line()

    def save(self) -> None:
        self.wb.save(self.path)
        print('Excel database has been saved successfully')

    def show_categories(self, limit: int):
        """

        :param limit:
        :return:
        """
        console.line()
        console.header('Showing categories')

        i = 0
        n = len(self.cats)

        for cat in self.cats:
            print('{:10}. {}'.format(i+1, cat))
            i += 1
            if i % limit == 0:
                print('Page {}/{}'.format(i // 10, (n + 9) // 10))
                print('Press enter to continue or enter -1 to exit')
                cmd = input('=> ')
                if cmd == '-1':
                    return

        console.line()

    def show_items(self, limit: int):
        i = 0
        n = self.products_count

        for ind, item in self.products.items():
            print('{:10}. [{}] => {} [{}-{}]'.format(
                i+1,
                item.uuid,
                item.name,
                item.production_date,
                item.expiration_date
            ))
            i += 1
            if i % limit == 0:
                print('Page {}/{}'.format(i // 10, (n + 9) // 10))
                print('Press enter to continue or enter -1 to exit')
                cmd = input('=> ')
                if cmd == '-1':
                    return

        console.line()




