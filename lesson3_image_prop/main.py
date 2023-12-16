import cv2
import numpy as np

img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR);

print(img.shape);

print(img.shape[0])
print(img.shape[1])
print(img.shape[2])


