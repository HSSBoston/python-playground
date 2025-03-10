import cv2, random, math, numpy as np
from extract_stars import extractStars
from star import Star
from crop_image import cropImage

def createScore(origFileNameWithoutExt, bigConstellation):
    stars, cropTop, cropBottom, leftMost, rightMost = cropImage(origFileNameWithoutExt, bigConstellation)
    sortedStars = sorted(stars, key=lambda x: x.center[0])

    for star in sortedStars:
        hPosition, hPositionNote = determineHorizontalPosition(star, bigConstellation,
                                                               cropTop, cropBottom, leftMost, rightMost)
        midiNoteNumber = determineVerticalPosition(star, cropTop, cropBottom, leftMost, rightMost)
        print(midiNoteNumber, hPosition, hPositionNote, star.shape )

def determineHorizontalPosition(star, bigConstellation, cropTop, cropBottom, leftMost, rightMost):
    if bigConstellation: divisionCountX = 8
    else:                divisionCountY = 4
    starX = star.center[0]
#     print(starX)
    
    currentX = leftMost
    for i in range(divisionCountX):
        if random.random() < 0.5:
            xMargin = math.floor((rightMost-leftMost)/divisionCountX)
        else:
            xMargin = math.ceil((rightMost-leftMost)/divisionCountX)
        previousX = currentX
        currentX += xMargin
        
        if starX > previousX and starX <= currentX:
            hPosition = i
            if starX < previousX + (currentX - previousX)/4:
                hPositionNote = "<<"
            elif starX < previousX + (currentX - previousX)*3/4:
                hPositionNote = "--"
            else:
                hPositionNote = "<<"
    return (hPosition, hPositionNote)

def determineVerticalPosition(star, cropTop, cropBottom, leftMost, rightMost):
    starY = star.center[1]

    yInterval = (cropBottom - cropTop)/24
    currentY = cropBottom
    for i in range(24):
        if starY > int(currentY - yInterval/2) and starY <= int(currentY + yInterval/2):
            vPosition = i
        
        if random.random() < 0.5: yMargin = math.floor(yInterval)
        else:                     yMargin = math.ceil(yInterval)
        currentY -= yMargin
    
    midiNoteNumber = vPosition+50
    return midiNoteNumber

if __name__ == "__main__":
#     origFileNamesWithoutExt = ["images/canis-major",
#                                "images/lyra",
#                                "images/canis-minor"]
# 
#     origFileNamesWithoutExt = ["images/aquila",
#                                "images/big-dipper",
#                                "images/cassiopeia",
#                                "images/cygnus",
#                                "images/orion"]

    createScore("images/cygnus", bigConstellation=True)





