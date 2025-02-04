import numpy as np
import cv2 as cv

video=cv.VideoCapture(0)
while True:
    ret,frame=video.read()
    cv.imshow('no one cares',frame)
    if cv.waitKey(5)==ord('x'):
        break

    edge=cv.Canny(frame,60,70)
    cv.imshow("the edges",edge)

video.release()
cv.destroyAllWindows()
