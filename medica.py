from uuid import uuid
from db import db


class Medica:
    def __init__(self):
        self.uuids = []

    def run(self):
        self.load()
        self.listen()
        self.save()

    def load(self):
        self.uuids = db.getUUIDS('./db/db.xlsx')

    def listen(self):
        pass

    def save(self):
        pass


medica = Medica()
medica.run()

print(medica.uuids)