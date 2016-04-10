# Krit Karan
# Sharpening an image


import cv2
import numpy as np


cv2.startWindowThread()
cv2.namedWindow("Original image")
cv2.namedWindow("Sharpen image")

imgIn = cv2.imread("name_of_image.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original image", imgIn)


#Create the identity filter, but with the 1 shifted to the right!
kernel = np.zeros( (9,9), np.float32)
kernel[4,4] = 2.0   #Identity, times two! 

#Create a box filter:
boxFilter = np.ones( (9,9), np.float32) / 81.0

#Subtract the two:
kernel = kernel - boxFilter


custom = cv2.filter2D(imgIn, -1, kernel)
cv2.imshow("Sharpen image", custom)


cv2.waitKey(0)