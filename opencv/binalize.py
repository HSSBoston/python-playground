import cv2
import numpy as np
import matplotlib.pyplot as plt


def binalizeImage(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Convert each pixel's color to grayscale.
    cv2.imwrite(origFileNameWithoutExt + "-gray.jpg", grayscaleImage)

    _, binaryImage = cv2.threshold(grayscaleImage, 127, 255, cv2.THRESH_BINARY)
        # binarization threshold: 127
        # If a pixel value is > threshold (127), the value becomes the max val (255).
        # Otherwise, it becomes 0. 
    cv2.imwrite(origFileNameWithoutExt + "-binary.jpg", binaryImage)
    
    return (grayscaleImage, binaryImage)

if __name__ == "__main__":
#     origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
    origFileNameWithoutExt = "images/orion"
    
    binalizeImage(origFileNameWithoutExt)
