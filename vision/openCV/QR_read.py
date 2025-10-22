import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode

# Initialise the camera so this program is using it
cap = cv.VideoCapture(0)            # 0 means from the 1st webcam connected to the computer

# Caputer the curent frame from the camera
ret, frame = cap.read() 

# Write the frame to given folder and set the file type
cv.imwrite('/home/pi4/Pictures/web_pic'+'.png', frame)
cap.release()       # Disconnect the camera from this program

img = cv.imread('/home/pi4/Pictures/web_pic.png')   #Import the image from the folder where it was saved
#img = cv.resize(img, (0, 0), fx = 2, fy =2)

for barcode in decode(img):
    print(barcode.rect)

cv.imshow('/home/pi4/Pictures/web_pic.png', img)    # Display the image

# Close the image when any key is pushed
cv.waitKey(0)
cv.destroyAllWindows()
