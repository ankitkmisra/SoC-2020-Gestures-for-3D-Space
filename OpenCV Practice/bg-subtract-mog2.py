import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)
    
    if ret:
        cv2.imshow('frame', fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()