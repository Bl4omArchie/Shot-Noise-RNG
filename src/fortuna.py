from Crypto.Cipher import AES
import hashlib


"""
Implementation of Fortuna PRNG

This script have tree classes:
- Fortuna: main class where you can generate and store random data
- Generator: converts a fixed-size state to arbitrarily long outputs
- Accumulator: handle RNG sources and seed the Generator

--
Source: Cryptography Engineering Design Principles and Practical Applications by Niels Ferguson, Bruce Schneier, Tadayoshi Kohno
Author: archie
"""


HASH = hashlib.sha256()



class Fortuna:
    def __init__(self, accumulator, generator):
        self.accumulator = accumulator
        self.generator = generator

    def write_random_data(self, filename):
        with open(filename, "a") as fp:
            fp.write(self.generate_random_data(64))

    def random(self, n):
        return self.generator.generate_pseudo_random_data(n)


class Generator():
    def __init__(self, mode=AES.MODE_EAX):
        self.state = None
        self.mode = mode

        self.Key = 0
        self.Counter = 0

    def seed(self, s):
        self.fortuna.Key = HASH.update(self.Key | s)
        self.iterate_counter()
        self.state = True

    def iterate_counter(self):
        pass

    def generate_blocks(self, num_block):
        assert self.Counter != 0
        r = b""

        for _ in range(num_block):
            cipher = AES.new(self.Key, self.mode)
            r, tag = cipher.encrypt_and_digest(self.Counter)
            self.iterate_counter()

        return r

    def generate_pseudo_random_data(self, n):
        assert 0 <= n <= pow(2, 20)

        r = self.generate_blocks(n//16)[:n]
        self.Key = self.generate_blocks(2)

        return r


class Accumulator():
    def __init__(self, block_size):
        self.block_byte_size = block_size
    
    def initialize_prng(self):
        pass

    def get_random_data(self):
        pass

    def add_event(self):
        pass