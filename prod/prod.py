class Product:
    """
        Product class just help the functionality of the application
        """
    def __init__(self, index: int, data: list):
        """
        :param index: the index of the product in the excel list
        :param data: an array of 4 properties of the product
            [uuid, name, production_date, expiration_date]
        """
        self.index = index
        self.uuid = data[0]
        self.name = data[1]
        self.production_date = data[2]
        self.expiration_date = data[3]


