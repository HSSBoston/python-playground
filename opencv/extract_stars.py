import cv2
import numpy as np
import matplotlib.pyplot as plt
from detect_contours import detectContours

def extractStars(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    contours, grayscaleImage, binaryImage = detectContours(origFileNameWithoutExt)
    
    stars = []
    
    for i, contour in enumerate(contours):
        arclen = cv2.arcLength(contour, True)
        approxPoly = cv2.approxPolyDP(contour, 0.015 * arclen, True)
#         print(approxPoly)
        
        if len(approxPoly) >= 8:
            (x,y), radius = cv2.minEnclosingCircle(approxPoly)
            center = (int(x), int(y))
            radius = int(radius)
            shapes.append([center, radius])
            if radius >= 8:
                shapeName = "big-circle"
                print("big circle", center, radius)
            else:
                shapeName = "small-circle"
                print("small circle", center, radius)
            star = Star(shapeName, center
                        center[0]-radius, center[0]+radius,
                        center[1]-radius, center[0]+radius)
        else:
            x, y, width, height = cv2.boundingRect(approxPoly)
            center = (int(x+(width/2)), int(y+(height/2)))
            halfSideLength = int((width + height)/4)
            star.
            stars.append([center, halfSideLength])
            
            print("rectangle", center, halfSideLength)

    return shapes, grayscaleImage, binaryImage

if __name__ == "__main__":
#     origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
    origFileNameWithoutExt = "images/orion"
    
    print(origFileNameWithoutExt)
    extractStars(origFileNameWithoutExt)
    

