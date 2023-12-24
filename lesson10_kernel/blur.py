import cv2
import numpy as np



img = cv2.imread("./_raw_img/grainy_noise.jpg");

height = img.shape[0]
width = img.shape[1]

# kernel = np.ones((11,11),np.float32) / 121
# dst = cv2.filter2D(img,-1,kernel)

# dst = cv2.blur(img,(11,11))


def showResult():
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img",int(width),int(height))
    cv2.imshow("img",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


showResult()
