import cv2
import numpy as np
import matplotlib.pyplot as plt
from detect_contours import detectContours
from star import Star

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
            (x,y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            if radius >= 8:
                shapeName = "big-circle"
            else:
                shapeName = "small-circle"
            star = Star(shapeName, center,
                        center[0]-radius, center[0]+radius,
                        center[1]-radius, center[1]+radius)
        else:
            x, y, width, height = cv2.boundingRect(contour)
            center = (int(x+(width/2)), int(y+(height/2)))
            halfSideLength = int((width + height)/4)
            star = Star("rectangle", center,
                        center[0]-halfSideLength, center[0]+halfSideLength,
                        center[1]-halfSideLength, center[1]+halfSideLength)

        stars.append(star)

    return stars, grayscaleImage, binaryImage

if __name__ == "__main__":
#     origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
    origFileNameWithoutExt = "images/orion"
    
    print(origFileNameWithoutExt)
    stars, _, _ = extractStars(origFileNameWithoutExt)
    
    for star in stars:
        print( star.shape, star.center,
               star.xLeft, star.xRight, star.yTop, star.yBottom)

