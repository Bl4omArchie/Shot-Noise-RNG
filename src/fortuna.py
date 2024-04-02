import hashlib

HASH = hashlib.sha256()

class Fortuna:
    def __init__(self):
        self.k = 0
        self.c = 0
        self.state = 0

    def seed(self, s):
        self.k = HASH.update(self.k | self.c)
        self.state = 1

    def generate_block(self):
        pass

    def increment_counter(self):
        pass