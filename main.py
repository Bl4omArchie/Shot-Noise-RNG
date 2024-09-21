from src.prng.fortuna import *
from src.aes_picture_encryption import Picture_encryption


if __name__ == "__main__":
    # AES picture encryption
    obj = Picture_encryption()
    obj.upload_folder("pictures/")
    
    if obj.encrypt(AES.MODE_OCB) == -1:
        raise ("Please upload pictures")


    # Fortuna PRNG
    accumulateur = Accumulator(block_size=1024)
    generator = Generator()
    fortuna = Fortuna(accumulateur, generator)


    nb_octets = 16
    nombres_aleatoires = fortuna.random(nb_octets)

    print(f"Nombres aléatoires ({nb_octets} octets): {nombres_aleatoires.hex()}")