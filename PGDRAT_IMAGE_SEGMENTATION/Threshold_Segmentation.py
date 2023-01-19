import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

image = cv2.imread("lena15.jpg", 0)

plt.figure(figsize=(8, 8))
plt.imshow(image, cmap="gray")
plt.axis("off")
plt.show()

flattened_image = image.reshape((image.shape[0] * image.shape[1],))

print(flattened_image.shape)

plt.figure()
sns.distplot(flattened_image, kde=True)
plt.show()

ret, thresh1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(8, 8))
plt.imshow(thresh1, cmap="binary")
plt.axis("off")
plt.show()