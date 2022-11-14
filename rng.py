from PIL import Image
import cv2


"""
The full-well capacity corresponds to the highest gray level value possible derived from the sensor resolution.
ex: for 8-bit sensor, it would be 2⁸-1 = 255 gray level values. 

"""

def graylevel_2_photoelectrons(gray_level, fullwell, bit_resolution):
    return gray_level * fullwell / (2^bit_resolution-1)

def photoelectrons_2_graylevel(number_of_electrons, bit_resolution, fullwell):
    return number_of_electrons * (2^bit_resolution-1) / fullwell;

def generate_random_bytes(bit_resolution):
    cap = cv2.VideoCapture(0)
    scaling_factor = 1

    while True:
        ret, frame = cap.read()
        input_image = Image.open(cv2.imshow('WindowName', frame))
        pixel_map = input_image.load()
        width, height = input_image.size


        # taking half of the width:
        for i in range(width//2):
            for j in range(height):
                
                # getting the RGB pixel value.
                r, g, b, p = input_image.getpixel((i, j))
                
                # Apply formula of grayscale:
                grayscale = (0.299*r + 0.587*g + 0.114*b)
        
                # setting the pixel value.
                pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))

        """
        fullwell = pow(2, bit_resolution)-1
        photo_electrons = graylevel_2_photoelectrons(pixel_value, fullwell, bit_resolution)
        GrayLevelPerPixel = bit_resolution * (photo_electrons/fullwell)
        """

        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        cv2.imshow('Webcam', frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate_random_bytes(16)