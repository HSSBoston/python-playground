import cv2, numpy as np
from binalize import binalizeImage

def detectContours(origFileNameWithoutExt):
    origFileName = origFileNameWithoutExt + ".jpg"
    image = cv2.imread(origFileName)

    grayscaleImage, binaryImage = binalizeImage(origFileNameWithoutExt)

    contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 3, cv2.LINE_AA)
        # -1: Draw all contours
        # (255, 0, 0): Coutour color (BGR)
        # 3: Thickness of a contour line
    cv2.imwrite(origFileNameWithoutExt + "-contours.jpg", image)
    print("Number of detected contours (stars):", len(contours))
    
    return (contours, grayscaleImage, binaryImage)


if __name__ == "__main__":
#     origFileNameWithoutExt = "images/aquila"
#     origFileNameWithoutExt = "images/big-dipper"
#     origFileNameWithoutExt = "images/canis-major"
#     origFileNameWithoutExt = "images/cassiopeia"
#     origFileNameWithoutExt = "images/cygnus"
#     origFileNameWithoutExt = "images/lyra"
#     origFileNameWithoutExt = "images/orion"
#     detectContours(origFileNameWithoutExt)

    origFileNamesWithoutExt = ["images/aquila",
                               "images/big-dipper",
                               "images/canis-major",
                               "images/cassiopeia",
                               "images/cygnus",
                               "images/lyra",
                               "images/orion",
                               "images/canis-minor"]
    for fileName in origFileNamesWithoutExt:
        detectContours(fileName)
