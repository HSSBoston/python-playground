import cv2
import numpy as np
import matplotlib.pyplot as plt
from extract_shapes import extractShapes

def cropImage(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    shapes, grayscaleImage, binaryImage = extractShapes(origFileNameWithoutExt)
    print(shapes)
    
    xLeft = 1000
    xRight = 0
    yTop = 1000
    yBottom = 0
    
    for shape in shapes:
        x = shape[0][0] - shape[1]
        if x < xLeft: xLeft = x
        
        x = shape[0][0] + shape[1]
        if x > xRight: xRight = x
        
        y = shape[0][1] - shape[1]
        if y < yTop: yTop = y
        
        y = shape[0][1] + shape[1]
        if y > yBottom: yBottom = y
    
    print(xLeft, xRight, yTop, yBottom)


if __name__ == "__main__":
    origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
#     origFileNameWithoutExt = "images/orion"
    
    print(origFileNameWithoutExt)
    cropImage(origFileNameWithoutExt)
    

