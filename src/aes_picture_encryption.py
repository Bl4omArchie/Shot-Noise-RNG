from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import os


class Picture_encryption():
    def __init__(self, format_file="RGBA", storage_folder="enc_pictures/"):
        self.format_file = format_file
        self.storage_folder = storage_folder
        self.set_images = {}

    def upload_image(self, picture_folder_name):
        """ 
        This function verify the existence and the format of the picture. 
        
        All the necessary data for encryption are stored in the dictionnary self.set_images as follow:
        {
            "path_picture+name_picture": [image, data, data_bytes],
            "example2": [image, data, data_bytes]
        }

        args:
            picture_folder_name: the path and name of your picture. Ex: ~/path/to/picture/picture.png

        """

        if os.path.isfile(picture_folder_name):
            image = Image.open(picture_folder_name)
            image = image.convert(self.format_file)
            data = np.array(image)
            data_bytes = data.tobytes()

            self.set_key = []
            self.set_images[picture_folder_name] = [image, data, data_bytes]
            self.set_enc_images = []
        else:
            return -1


    def upload_folder(self, folder):
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                self.upload_image(os.path.join(folder, filename))
    

    def pad_image(self, data):
        pad_len = 16 - (len(data) % 16)
        return data + b'\0' * pad_len


    def encrypt(self, aes_mode):
        if self.set_images == []:
            return -1

        if self.set_key == []:
            for i in range(len(self.set_images)):
                self.set_key.append(os.urandom(16))


        for filename, data_image in self.set_images.items():
            cipher = AES.new(self.set_key[i], aes_mode)

            padded_data = self.pad_image(data_image[2])
            encrypted_data = cipher.encrypt(padded_data)
            
            encrypted_array = np.frombuffer(encrypted_data[:len(data_image[2])], dtype=np.uint8)
            encrypted_array = encrypted_array.reshape(data_image[1].shape)
            
            encrypted_image = Image.fromarray(encrypted_array)
            encrypted_image.save(f"{self.storage_folder}encrypted_{i}.png")
        

    def decrypt(self):
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