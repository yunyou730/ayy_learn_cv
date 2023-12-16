import cv2
import numpy as np

img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_GRAYSCALE);
cv2.imwrite("./_produce/badge_gray.jpeg",img);


img = cv2.imread("./_produce/badge_gray.jpeg",cv2.IMREAD_COLOR);
wnd = cv2.imshow("test image",img);
while True:
    if cv2.waitKey(0) == ord('q'):
        break;
cv2.destroyWindow(wnd)
