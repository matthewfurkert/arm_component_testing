import cv2 as cv

# if error message use in terminal:
# export DISPLAY=localhost:10.0

img = cv.imread('/Users/furky/Pictures/cat.jpeg')

cv.imshow('cat', img)

cv.waitKey(0)