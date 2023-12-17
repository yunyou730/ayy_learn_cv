import cv2
import numpy as np


def filterWithBit(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([78,43,46])
    upper_blue = np.array([99,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    res = cv2.bitwise_and(frame,frame,mask = mask)

    return frame,mask,res,hsv


frame = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)

while True:
    frame,mask,res,hsv = filterWithBit(frame)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)        
    cv2.imshow("hsv",hsv)
    if cv2.waitKey(1) == ord('q'):
        break;

cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret,frame = cap.read();
#     if ret:

#         frame,mask,res = filterWithBit(frame)
#         cv2.imshow("video",frame)
#         cv2.imshow("res",res)
#         cv2.imshow("mask",mask)

#         if cv2.waitKey(1) == ord('q'):
#             break
#     else:
#         break
    
# cap.release()
# cv2.destroyAllWindows()
