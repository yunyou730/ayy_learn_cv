import cv2
import numpy as np

img = cv2.imread("./_raw_img/woman.jpeg");

height = img.shape[0]
width = img.shape[1]

dst = cv2.bilateralFilter(img,11,40,40)



def showResult():
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img",int(width),int(height))
    cv2.imshow("img",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.imshow("origin",img)
showResult()
