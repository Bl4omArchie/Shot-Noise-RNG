from Crypto.Cipher import AES
import hashlib


"""
Implementation of Fortuna PRNG in python

This script have tree classes:
- Fortuna: main class where you can generate and store random data
- Generator: converts a fixed-size state to arbitrarily long outputs
- Accumulator: handle RNG sources and seed the Generator

--
Usage:
- The max byte size you can ask Fortuna for a random number is 2**20 as specified in my documentation
- Call random() to get a random number of size N or call write_random() if you want to write the generated number in a file.

--
Source: Cryptography Engineering Design Principles and Practical Applications by Niels Ferguson, Bruce Schneier, Tadayoshi Kohno
Author: archie
"""


HASH = hashlib.sha256()



class Fortuna:
    def __init__(self, accumulator, generator):
        self.accumulator = accumulator
        self.generator = generator

    def random(self, n):
        return self.generator.generate_pseudo_random_data(n)
    
    def write_random(self, filename, n):
        with open(filename, "a") as fp:
            fp.write(self.generate_pseudo_random_data(n))


class Generator():
    def __init__(self, mode=AES.MODE_EAX):
        self.state = None
        self.mode = mode


    def initialize_generator(self):
        self.Key = 0
        self.Counter = 0
        return (self.Key, self.Counter)

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
        """
        Limit the output length to reduce the statistical deviation from perfectly random outputs. 
        Also ensure that the length is not negative.
        """
        assert 0 <= n <= pow(2, 20)

        r = self.generate_blocks(n//16)[:n]
        self.Key = self.generate_blocks(2)

        return r


class Accumulator():
    def __init__(self, generator, block_size):
        self.generator = generator
        self.block_byte_size = block_size


    def initialize_prng(self):
        self.P = []
        for _ in range(32):
            self.P.append(0)
        
        self.reseed_count = 0
        G = self.generator.initialize_generator()
        return  (G, self.reseed_count, self.P)


    def get_random_data(self):
        pass

    def add_event(self):
        pass