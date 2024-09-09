import cv2
import numpy as np
import matplotlib.pyplot as plt

origFileName = "shapes.jpg"
image = cv2.imread(origFileName)

grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert each pixel's color to grayscale.
cv2.imwrite("shapes-gray.jpg", grayscaleImage)


_, binaryImage = cv2.threshold(grayscaleImage, 127, 255, cv2.THRESH_BINARY)
    # binarization threshold: 127
    # If a pixel value is > threshold (127), the value becomes the max val (255).
    # Otherwise, it becomes 0. 
cv2.imwrite("shapes-binary.jpg", binaryImage)

contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
    # -1: draw all contours
    # (255, 0, 0): Coutour color
    # 3: Thickness of a contour line
# cv2.imwrite("shapes-binary.jpg", binaryImage)
# 
# cv2.approxPolyDP

print(len(contours))

# plt.imshow(image)
# plt.show()
