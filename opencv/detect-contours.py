import cv2
import numpy as np
import matplotlib.pyplot as plt
from binalize import binalizeImage

def detectContours(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    grayscaleImage, binaryImage = binalizeImage(origFileNameWithoutExt)

    contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
        # -1: Draw all contours
        # (255, 0, 0): Coutour color
        # 3: Thickness of a contour line
    cv2.imwrite(origFileNameWithoutExt + "-contours.jpg", image)
    print("Number of detected contours:", len(contours))


if __name__ == "__main__":
    # origFileNameWithoutExt = "big-dipper"
    origFileNameWithoutExt = "red"
    detectContours(origFileNameWithoutExt)

