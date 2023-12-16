import cv2
import numpy as np

def borderConst():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    border_size = 50

    img2 = cv2.copyMakeBorder(img,border_size,border_size,border_size,border_size,cv2.BORDER_CONSTANT,value = (0,255,255))

    cv2.imshow("expand",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# borderConst();    


def borderReflect():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    border_size = 100

    img2 = cv2.copyMakeBorder(img,border_size,border_size,border_size,border_size,cv2.BORDER_REFLECT)

    cv2.imshow("expand",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


# borderReflect()
    
def borderReflect101():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    border_size = 100

    img2 = cv2.copyMakeBorder(img,border_size,border_size,border_size,border_size,cv2.BORDER_REFLECT_101)

    cv2.imshow("expand",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

# borderReflect101();


def borderReplicate():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    border_size = 100

    img2 = cv2.copyMakeBorder(img,border_size,border_size,border_size,border_size,cv2.BORDER_REPLICATE)

    cv2.imshow("expand",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

# borderReplicate();

def borderWrap():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    border_size = 100

    img2 = cv2.copyMakeBorder(img,border_size,border_size,border_size,border_size,cv2.BORDER_WRAP)

    cv2.imshow("expand",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

borderWrap();


