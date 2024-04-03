from src.prng.fortuna import *


if __name__ == "__main__":
    accumulateur = Accumulator(block_size=1024)
    generator = Generator()
    fortuna = Fortuna(accumulateur, generator)


    nb_octets = 16
    nombres_aleatoires = fortuna.random(nb_octets)

    print(f"Nombres aléatoires ({nb_octets} octets): {nombres_aleatoires.hex()}")