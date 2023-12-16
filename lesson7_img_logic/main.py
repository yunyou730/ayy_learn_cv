import cv2
import numpy as np

def test1():
    #img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR);
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_GRAYSCALE);
    img = cv2.bitwise_not(img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
# test1()


def testSlice():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR);
    (y,x) = img.shape[0:2]
    cv2.imshow("img",img)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img2 = img[:int(y/2),:int(x/2)]
    cv2.imshow("img2",img2)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()    

    img3 = img[int(y/2):,int(x/2):]
    cv2.imshow("img3",img3);
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()    

testSlice();
