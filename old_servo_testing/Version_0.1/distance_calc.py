import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
from math import sqrt

img = cv.imread('/home/pi4/Pictures/web_pic.png')   #Import the image from the folder where it was saved
#img = cv.resize(img, (0, 0), fx = 2, fy =2)

for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2)) # Reshaping the array with as many rows as necessary, 1 column, which has 2 data values
    cv.polylines(img,[pts],True,(255,0,255),5) # making a box around the qr code


#Define object specific variables  
# Camera specifications
focal = 4               # focal length of logitech c270 camera (mm)
sen_height_mm = 4.15    # camera sensor height (mm) *tune this value
# QR Code Specification
qr_height_mm = 55       # height of qr code (mm)
qr_width_mm = 55        # width of qr code (mm)
# Image Data
img_height_px = (img.shape[0])      # image pixel height also equavilent to the sensor height
img_width_px = (img.shape[1])       # image pixel width also equavilent to the sensor width
qr_height_px = barcode.rect[3]  # height of the detected qr code in pixels
qr_width_px = barcode.rect[2]   # width of the detected qr code in pixels
qr_left_px = barcode.rect[0]    # distace from the left hand side of the image to left hand side of the qr code in pixels

#cv.imshow('/home/pi4/Pictures/web_pic.png', img)    # Display the image

#find the distance from then camera
dist = (focal*qr_height_mm*img_height_px)/(sen_height_mm*qr_height_px)

# Calculating number of x direction pixels between centre of image and centre of bacode
# A negative output means the barcode is located on the left hand side of the image
dist_x_px = -((img_width_px/2)-(qr_left_px+(qr_width_px/2)))

# Calculating the x distance from centre of image to centre of barcode
# Formula is derived from the ratio: qr_width_px/qr_width_mm = dist_x_px/dist_x_mm
dist_x_mm = (qr_width_mm * dist_x_px)/qr_width_px
dist_y_mm = sqrt(dist**2 - dist_x_mm**2)    # Using pythag to calculate x distance

print(dist)
print(dist_x_mm)
print(dist_y_mm)
    
# Close the image when any key is pushed
cv.waitKey(0)
cv.destroyAllWindows()