import random


class UUID:
    """
    All processes related to uuid are handled by an instance of
    this class.
    """
    def __init__(self, salt_path: str, length: int):
        """
        :param salt_path: the file containing the salt
        :param length: the resulting uuid length
        """
        self.salt = open(salt_path, 'r').read()
        self.length = length

    def generate(self, uuids: list) -> str:
        """
        :param uuids: the list containing all uuids
        :return: a random non-repetitive uuid
        :rtype: str
        """
        chars = []
        for i in range(self.length):
            chars.append(random.choice(self.salt))
        result = ''.join(chars)
        return self.generate() if result in uuids else result

    def new(self, uuids: list) -> str:
        """
        :param uuids: the list containing all uuids
        :return: generates a new uuid
        :rtype: str
        """
        result = self.generate(uuids)
        uuids.add(result)
        return result

