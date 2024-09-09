import cv2
import numpy as np
import matplotlib.pyplot as plt
from detect_contours import detectContours

def extractShapes(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    contours, grayscaleImage, binaryImage = detectContours(origFileNameWithoutExt)
    
    for i, contour in enumerate(contours):
        arclen = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * arclen, True)
        print(len(approx))




if __name__ == "__main__":
    # origFileNameWithoutExt = "images/big-dipper"
    origFileNameWithoutExt = "images/red"
    
    extractShapes(origFileNameWithoutExt)
    
