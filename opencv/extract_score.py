import cv2, random, math, numpy as np, matplotlib.pyplot as plt
from extract_stars import extractStars
from star import Star
from extract_constellation_size import extractConstellationSize

def extractScore(origFileNameWithoutExt):
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
    
    currentX = 0
    for i in range(8):
        if i == 4:
            cv2.line(croppedBinaryImage, (currentX,0), (currentX,croppedHeight-1), (0,0,255))
        else:
            cv2.line(croppedBinaryImage, (currentX,0), (currentX,croppedHeight-1), (255,0,0))
        if random.random() < 0.5:
            xMargin = math.floor(croppedWidth/8)
        else:
            xMargin = math.ceil(croppedWidth/8)
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
        
#         cv2.line(croppedBinaryImage, (croppedWidth-1,0), (croppedWidth-1,croppedHeight-1), (255,0,0))
    
    cv2.imwrite(origFileNameWithoutExt + "-binary-cropped.jpg", croppedBinaryImage)
    
    

if __name__ == "__main__":
    origFileNamesWithoutExt = ["images/aquila",
                               "images/big-dipper",
                               "images/canis-major",
                               "images/cassiopeia",
                               "images/cygnus",
                               "images/lyra",
                               "images/orion",
                               "images/canis-minor"]
    for fileName in origFileNamesWithoutExt:
        cropImage(fileName)
    







