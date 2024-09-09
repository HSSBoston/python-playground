import cv2
import numpy as np
import matplotlib.pyplot as plt

origFileNameWithoutExt = "big-dipper"
# origFileNameWithoutExt = "red"

origFileName = origFileNameWithoutExt + ".jpg"
image = cv2.imread(origFileName)
# plt.imshow(image)
# plt.show()

grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert each pixel's color to grayscale.
cv2.imwrite(origFileNameWithoutExt + "-gray.jpg", grayscaleImage)

# grascaleBlueImage = cv2.blur(grayscaleImage,(9,9))
# cv2.imwrite("big-dipper-gray-blur.jpg", grascaleBlueImage)

_, binaryImage = cv2.threshold(grayscaleImage, 127, 255, cv2.THRESH_BINARY)
    # binarization threshold: 127
    # If a pixel value is > threshold (127), the value becomes the max val (255).
    # Otherwise, it becomes 0. 
cv2.imwrite(origFileNameWithoutExt + "-binary.jpg", binaryImage)

contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
    # -1: Draw all contours
    # (255, 0, 0): Coutour color
    # 3: Thickness of a contour line
cv2.imwrite(origFileNameWithoutExt + "-contours.jpg", image)
print("Number of contours", len(contours))

# cv2.imshow("contours", image)
# plt.imshow(image)
# plt.show()

# cv2.approxPolyDP


