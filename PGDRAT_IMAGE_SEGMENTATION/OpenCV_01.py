'''
# pip3 install opencv-python
# Import OpenCV
import cv2

# Access target image
image = cv2.imread("Images/lena15.jpg")

# Display Target Image
cv2.imshow("Image", image)

# Write Text On An Image
cv2.putText(image, "Hello",(200,200), cv2.FONT_HERSHEY_SIMPLEX, 6, (30,105,210),40)

# Display Image with text
cv2.imshow("Image2", image)

# Write Image
cv2.imwrite("Write_Images/Image0002.jpg", image)

# Wait for a key to be pressed and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2

# Access target image
image = cv2.imread("Images/Image_Dog.jpg")

image = cv2.resize(image, (640,480))

# Change Image Color Scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, threshold_image = cv2.threshold(gray_image, 150,200,10)

print(ret)

cv2.imshow("Gray Scale Image", gray_image)
cv2.imshow("Threshold Image", threshold_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import cv2

# Access target image
image = cv2.imread("Images/Image_Dog.jpg")

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.resize(image, (640,480))

# (h, w) = image.shape
(h, w, d) = image.shape

print(image.shape)

center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))

cv2.imshow("Show Rotated Image",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()