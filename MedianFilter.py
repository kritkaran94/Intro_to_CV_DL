# Krit Karan
# Adding median filter in an image


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('name_of_image.png')

median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original image')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred image')
plt.xticks([]), plt.yticks([])
plt.show()