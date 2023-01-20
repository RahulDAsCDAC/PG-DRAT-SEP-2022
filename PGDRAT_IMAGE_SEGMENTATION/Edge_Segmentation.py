import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from skimage import filters
import skimage

warnings.filterwarnings("ignore")

image = cv2.imread("Images/lena15.jpg", 0)

plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.axis("off")
plt.show()

# Sobel Edge
sobel_image = filters.sobel(image)

plt.figure(figsize=(8, 8))
plt.imshow(sobel_image)
plt.axis("off")
plt.show()

# Robert Edge
roberts_image = filters.roberts(image)

plt.figure(figsize=(8, 8))
plt.imshow(roberts_image)
plt.axis("off")
plt.show()

# Prewitt Edge
prewitt_image = filters.prewitt(image)
     
plt.figure(figsize=(8, 8))
plt.imshow(prewitt_image)
plt.axis("off")
plt.show()