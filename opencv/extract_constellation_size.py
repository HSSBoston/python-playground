import cv2, numpy as np, matplotlib.pyplot as plt
from extract_stars import extractStars
from star import Star

def extractConstellationSize(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    stars, grayscaleImage, binaryImage = extractStars(origFileNameWithoutExt)
    
    leftMost = 1000
    rightMost = 0
    topMost = 1000
    bottomMost = 0

#     for star in stars:
#         print(star.shape, star.center,
#               star.xLeft, star.xRight, star.yTop, star.yBottom)

    for star in stars:
        if star.xLeft < leftMost: leftMost = star.xLeft
        if star.xRight > rightMost: rightMost = star.xRight
        if star.yTop < topMost: topMost = star.yTop
        if star.yBottom > bottomMost: bottomMost = star.yBottom
    
#     print(leftMost, rightMost, topMost, bottomMost)
    return (stars, leftMost, rightMost, topMost, bottomMost)

def extractMaxConstellationHeight(origFileNamesWithoutExt):
    maxHeight = 0
    for fileName in origFileNamesWithoutExt:
        stars, leftMost, rightMost, topMost, bottomMost = extractConstellationSize(fileName)
        height = bottomMost - topMost
        print(leftMost, rightMost, topMost, bottomMost)
        print("Height", height)
        if height > maxHeight:
            maxHeight = height
    return maxHeight

if __name__ == "__main__":
    origFileNamesWithoutExt = ["images/aquila",
                               "images/big-dipper",
                               "images/canis-major",
                               "images/cassiopeia",
                               "images/cygnus",
                               "images/lyra",
                               "images/orion",
                               "images/canis-minor"]
    maxHeight = extractMaxConstellationHeight(origFileNamesWithoutExt)
    print("Max height", maxHeight)
    





