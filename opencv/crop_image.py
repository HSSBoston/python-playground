import cv2, random, math, numpy as np, matplotlib.pyplot as plt
from extract_stars import extractStars
from star import Star
from extract_constellation_size import extractConstellationSize

def cropImage(origFileNameWithoutExt, bigConstellation):
    binaryFileName = origFileNameWithoutExt + "-binary" + ".jpg"
    binaryImage = cv2.imread(binaryFileName)
    height = binaryImage.shape[0]
    width = binaryImage.shape[1]
#     print(height,width)
    maxConstellationHeight = 322
    
    stars, leftMost, rightMost, topMost, bottomMost = extractConstellationSize(origFileNameWithoutExt)
    verticalMiddle = int((bottomMost + topMost)/2)
    cropTop = int(verticalMiddle-(maxConstellationHeight/2))
    cropBottom = int(verticalMiddle+(maxConstellationHeight/2))
    
    croppedBinaryImage = binaryImage[cropTop:cropBottom, leftMost:rightMost]
#     cv2.imwrite(origFileNameWithoutExt + "-binary-cropped.jpg", croppedBinaryImage)
    
    croppedHeight = croppedBinaryImage.shape[0]
    croppedWidth = croppedBinaryImage.shape[1]
    
    if bigConstellation:
        divisionCountX = 8
    else: 
        divisionCountX = 4
    currentX = 0
    for i in range(divisionCountX):
        if i == divisionCountX/2:
            cv2.line(croppedBinaryImage, (currentX,0), (currentX,croppedHeight-1), (0,0,255))
        else:
            cv2.line(croppedBinaryImage, (currentX,0), (currentX,croppedHeight-1), (255,0,0))
        if random.random() < 0.5:
            xMargin = math.floor(croppedWidth/divisionCountX)
        else:
            xMargin = math.ceil(croppedWidth/divisionCountX)
        currentX += xMargin
    
    currentY = 0
    for i in range(13):
        if i >= 4 and i <= 8:
            cv2.line(croppedBinaryImage, (0,currentY), (croppedWidth-1,currentY), (0,0,255))
        else:
            cv2.line(croppedBinaryImage, (0,currentY), (croppedWidth-1,currentY), (255,0,0))
        if random.random() < 0.5:
            yMargin = math.floor(croppedHeight/12)
        else:
            yMargin = math.ceil(croppedHeight/12)
        currentY += yMargin
    
    for star in stars:
        x, y = star.center
        adjustedX = x - leftMost
        adjustedY = y - cropTop
        croppedBinaryImage[adjustedY, adjustedX] = [0, 255, 0]
        croppedBinaryImage[adjustedY, adjustedX-1] = [0, 255, 0]
        croppedBinaryImage[adjustedY, adjustedX+1] = [0, 255, 0]
        croppedBinaryImage[adjustedY-1, adjustedX] = [0, 255, 0]
        croppedBinaryImage[adjustedY+1, adjustedX] = [0, 255, 0]
    
    cv2.imwrite(origFileNameWithoutExt + "-binary-cropped.jpg", croppedBinaryImage)
    return (stars, cropTop, cropBottom, leftMost, rightMost)
    

if __name__ == "__main__":
    origFileNamesWithoutExt = ["images/canis-major",
                               "images/lyra",
                               "images/canis-minor"]
    for fileName in origFileNamesWithoutExt:
        cropImage(fileName, bigConstellation=False)

    origFileNamesWithoutExt = ["images/aquila",
                               "images/big-dipper",
                               "images/cassiopeia",
                               "images/cygnus",
                               "images/orion"]
    for fileName in origFileNamesWithoutExt:
        cropImage(fileName, bigConstellation=True)
 






