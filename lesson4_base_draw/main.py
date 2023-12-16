import cv2
import numpy as np
import math

#img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR);
img = np.zeros((512,512,3),np.uint8);   # create 512x512, 3 channels, uint8 , tuple 

h = img.shape[0]
w = img.shape[1]

cv2.line(img,(0,0),(w,h),(0,255,0),3);
cv2.rectangle(img,(math.floor(w * 0.3),math.floor(h * 0.3)),(math.floor(w * 0.8),math.floor(h * 0.8)),(0,0,255),3)

wind = cv2.imshow("test",img)

while True:
    if cv2.waitKey(0) == ord('q'):
        break;

cv2.destroyWindow(wind)
