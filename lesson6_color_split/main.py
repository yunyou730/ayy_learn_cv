import cv2
import numpy as np
import math

def test_color_split():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    (b,g,r) = cv2.split(img)


    height = img.shape[0]
    width = img.shape[1]
    img2 = np.zeros((height,width,3),np.uint8);   # create 512x512, 3 channels, uint8 , tuple 


    cv2.imshow("channel_b",b)
    cv2.imshow("channel_g",g)
    cv2.imshow("channel_r",r)


    cv2.merge((b,g,r),img);
    cv2.merge((r,g,b),img2);

    cv2.imshow("merged",img);
    cv2.imshow("merged_wrong",img2);    

    while True:
        if cv2.waitKey(0) == ord('q'):
            break;
    cv2.destroyAllWindows()
        
test_color_split()


def test_gray_img():
    img = cv2.imread("./_raw_img/badge.jpeg",cv2.IMREAD_COLOR)
    # img = cv2.imread("./_produce/badge_gray.jpeg",cv2.IMREAD_COLOR);

    rows = img.shape[0]
    cols = img.shape[1]
    print("img size:" + str(rows) + " x " + str(cols))

    splitted_data = cv2.split(img)
    print("splitted_data len:" + str(len(splitted_data)))
    for i in range(0,len(splitted_data)):
        channel = splitted_data[i]
        print("channel " + str(i) + " len " + str(len(channel)))

    for y in range(rows):
        for x in range(cols):
            b = splitted_data[0][y][x]
            g = splitted_data[1][y][x]
            r = splitted_data[2][y][x]
            assert(b == g and b == r)

    print("all pixels rgb are equal")
