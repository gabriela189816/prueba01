import numpy as np
import cv2 as cv

width = 1280
height = 720
video0 = cv.VideoCapture(2)
video0.set(cv.CAP_PROP_FRAME_WIDTH, width)
video0.set(cv.CAP_PROP_FRAME_HEIGHT, height)

video1 = cv.VideoCapture(6)
video1.set(cv.CAP_PROP_FRAME_WIDTH, width)
video1.set(cv.CAP_PROP_FRAME_HEIGHT, height)

video2 = cv.VideoCapture(10)
video2.set(cv.CAP_PROP_FRAME_WIDTH, width)
video2.set(cv.CAP_PROP_FRAME_HEIGHT, height)


while True:
    ret0, frame0 = video0.read()
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    if (ret0):
        cv.imshow('camera 0', frame0)

    if (ret1):
        cv.imshow('camera 1', frame1)

    if (ret2):
        cv.imshow('camera 2', frame2)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video0.release()
video1.release()
video2.release()
cv.destroyAllWindows()