import random


class UUID:
    def __init__(self, salt_path, length):
        """
        :param salt_path: str
        :param length: int
        :return: None
        """
        self.salt = open(salt_path, 'r').read()
        self.length = length
        self.uuids = set()

    def generate(self) -> str:
        """
        :return: a random non-repetitive uuid
        :rtype: str
        """
        result = []
        for i in range(self.length):
            result.append(random.choice(self.salt))
        return self.generate() if result in self.uuids else ''.join(result)

    def new(self) -> str:
        """
        :return: generates a new uuid
        """
        result = self.generate()
        self.uuids.add(result)
        return result


def generate(salt, length):
    """
    generate a random
    :param length: int
    :param salt: str
    :return: str
    """
    result = []
    for i in range(length):
        result.append(random.choice(salt))
    return ''.join(result)


def get(uuids: set, length, satlPath) -> str:
    """
    :param satlPath: str
    :param uuids: set
    :param length: int
    :return:
    """
    salt = open(satlPath, 'r').read()
    result = generate(salt, length)
    while result in uuids:
        result = generate(salt, length)
    uuids.add(result)
    return result

