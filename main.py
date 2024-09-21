from src.fortuna import *
from src.picture_encryption import App_Picture_Encryption






if __name__ == "__main__":
    # AES picture encryption
    obj = App_Picture_Encryption()
    obj.upload_folder("pictures/")
    obj.encrypt_picture()


    # Fortuna PRNG
    """
    accumulateur = Accumulator(block_size=1024)
    generator = Generator()
    fortuna = Fortuna(accumulateur, generator)


    nb_octets = 16
    nombres_aleatoires = fortuna.random(nb_octets)

    print(f"Nombres aléatoires ({nb_octets} octets): {nombres_aleatoires.hex()}")
    """