import cv2
import numpy as np
import matplotlib.pyplot as plt
from extract_shapes import extractShapes

def cropImage(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    shapes, grayscaleImage, binaryImage = extractShapes(origFileNameWithoutExt)
    
    print(shapes)


if __name__ == "__main__":
#     origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
    origFileNameWithoutExt = "images/orion"
    
    print(origFileNameWithoutExt)
    extractShapes(origFileNameWithoutExt)
    

