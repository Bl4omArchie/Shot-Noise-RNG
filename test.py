from PIL import Image
import cv2


cap = cv2.VideoCapture(0)
scaling_factor = 1

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imwrite('capture.jpg', frame)

    input_image = Image.open("capture.jpg")
    width, height = input_image.size
    
    for i in range(2):
        for j in range(2):
            print (input_image.getpixel((i, j)))
            print ("\n")

    print (rgb[0][0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
