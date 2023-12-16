import cv2 as cv

img = cv.imread("_raw_img/me.jpeg");
cv.imshow("Display window",img);
k = cv.waitKey(0);