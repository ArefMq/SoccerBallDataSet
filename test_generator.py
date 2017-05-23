#!/usr/bin/python

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)

count = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    count += 1
    if (count == 30):
        p = './data/fram_' + str(time.time()) + ".png"
        cv2.imwrite(p, frame)
        cv2.imshow('frame - Save',gray)
        count = 0
    else:
        cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
