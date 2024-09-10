import cv2, random, math, numpy as np, matplotlib.pyplot as plt
from extract_stars import extractStars
from star import Star
from crop_image import cropImage

def extractScore(origFileNameWithoutExt, bigConstellation):
    constellationName = split(origFileNameWithoutExt, "/")[1]
    
    stars, cropTop, cropBottom, leftMost, rightMost = cropImage(origFileNameWithoutExt)
    sortedStars = sorted(stars, key=lambda x: x.center[0])

    for star in sortedStars:
        print(star.center[0])
        determineHorizontalPosition(star, cropTop, cropBottom, leftMost, rightMost)

def determineHorizontalPosition(star, cropTop, cropBottom, leftMost, rightMost):
    if (rightMost-leftMost) < 150:
    
    else:
    
    starX = star.center[0]
    
    currentX = 0
    for i in range(8):
        if random.random() < 0.5:
            xMargin = math.floor((rightMost-leftMost)/8)
        else:
            xMargin = math.ceil(croppedWidth/8)
        currentX += xMargin
        
        if starX <= currentX 




    
    

    
if __name__ == "__main__":
#     origFileNamesWithoutExt = ["images/canis-major",
#                                "images/lyra",
#                                "images/canis-minor"]
#     for fileName in origFileNamesWithoutExt:
#         cropImage(fileName, bigConstellation=False)
# 
#     origFileNamesWithoutExt = ["images/aquila",
#                                "images/big-dipper",
#                                "images/cassiopeia",
#                                "images/cygnus",
#                                "images/orion"]
#     for fileName in origFileNamesWithoutExt:
#         cropImage(fileName, bigConstellation=True)

    extractScore("images/cygnus", bigConstellation=True)





