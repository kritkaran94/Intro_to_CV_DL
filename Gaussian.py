# Krit Karan
# Smoothing an image


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('name_of_image.png')

blur = cv2.GaussianBlur(img,(5,5),0)  # Kernel of size 5 * 5

plt.subplot(121),plt.imshow(img),plt.title('Original image')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred image')
plt.xticks([]), plt.yticks([])
plt.show()