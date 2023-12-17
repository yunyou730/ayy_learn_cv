import cv2
import numpy as np


def cameraVideo():
    cap = cv2.VideoCapture(0)
    print(type(cap))

    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("video",frame)
            cv2.imshow("video_gray",gray)
        if cv2.waitKey(1) == ord('q'):
            break;

    cv2.destroyAllWindows()
    cap.release()

# cameraVideo()


def saveVideo():
    cap = cv2.VideoCapture(0)
    # fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("./_produce/test2.avi",fourcc,20.0,(640,480))
    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            frame = cv2.flip(frame,1)
            out.write(frame)
            cv2.imshow("frame",frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

saveVideo()
