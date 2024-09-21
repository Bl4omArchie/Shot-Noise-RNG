from Crypto.Cipher import AES
from src.aes import AES_Encryption
from PIL import Image
import numpy as np

import os



class App_Picture_Encryption(AES_Encryption):
    def __init__(self, aes_mode=AES.MODE_ECB, format_file="RGBA", storage_folder="enc_pictures/"):
        self.format_file = format_file
        self.storage_folder = storage_folder
        self.set_images = {}
        
        AES_Encryption.__init__(self, aes_mode)
        
        if not os.path.exists(storage_folder):
            os.mkdir(storage_folder)
            
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
                
    def encrypt_picture(self):
        if self.set_images == []:
            raise ValueError("Please upload pictures")
            return -1

        if self.set_key == []:
            for i in range(len(self.set_images)):
                self.set_key.append(os.urandom(16))
        
        i = 0
        for filename, data_image in self.set_images.items():
            self.aes_encrypt(f"{self.storage_folder}encrypted_pic_{i}.png", self.set_key[i], data_image[1], data_image[2])
            i += 1
    
    def decrypt_picture(self):
        pass