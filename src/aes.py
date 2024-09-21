from Crypto.Cipher import AES
from PIL import Image
import numpy as np


class AES_Encryption():
    def __init__(self, aes_mode):
        self.aes_mode = aes_mode


    def pad_image(self, data):
        pad_len = 16 - (len(data) % 16)
        return data + b'\0' * pad_len


    def aes_encrypt(self, result_picture_name, key, data, data_bytes):
        cipher = AES.new(key, self.aes_mode)

        padded_data = self.pad_image(data_bytes)
        encrypted_data = cipher.encrypt(padded_data)
        
        encrypted_array = np.frombuffer(encrypted_data[:len(data_bytes)], dtype=np.uint8)
        encrypted_array = encrypted_array.reshape(data.shape)
        
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(result_picture_name)
        
        return encrypted_image
        

    def aes_decrypt(self):
        data = np.array(encrypted_image)
        data_bytes = data.tobytes()
        
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_data = cipher.decrypt(data_bytes)
        
        # Remove padding
        decrypted_data = decrypted_data[:data.size]
        decrypted_array = np.frombuffer(decrypted_data, dtype=np.uint8)
        decrypted_array = decrypted_array.reshape(data.shape)
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save("decrypted_image_corrected.png")