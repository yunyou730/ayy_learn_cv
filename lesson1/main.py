import cv2
import numpy as np

# D = (F * W) / P
KNOWN_WIDTH = 23.36
KNOWN_HEIGHT = 8.27
KNOWN_DISTANCE = 7.7
FOCAL_LENGTH = 543.45

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*"XVID");
out = cv2.VideoWriter('./_produce/latest.avi',fourcc,20.0,(640,480));

while True:
    ret,img = cap.read();
    img = cv2.flip(img,1);
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

    # gaussian
    blurred = cv2.GaussianBlur(gray,(5,5),0);
    edges = cv2.Canny(img,35,125);

    # 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10));

    #
    closed = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
    closed = cv2.erode(closed,None,iterations = 4);
    closed = cv2.dilate(closed,None,iterations = 4);

    # contours
    contours,hierarchy = cv2.findContours(closed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);

    cnt = max(contours,key = cv2.contourArea);
    img = cv2.drawContours(img,[cnt], - 1,(0,255,0),3);
    rect = cv2.minAreaRect(cnt);

    # distance
    distance = (KNOWN_WIDTH * FOCAL_LENGTH) / rect[1][0];

    # display numbers
    cv2.putText(img,"%.2fcm"%(distance * 2.54),(img.shape[1] - 300,img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,255),3);

    # save video
    out.write(img);

    # display image
    cv2.imshow('img',img);
    cv2.imshow('edges',edges)
    cv2.imshow("closed",closed);

    if cv2.waitKey(1) == ord('q'):
        break;

cap.release();
out.release();
cv2.destroyAllWindows()






