import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()
    
    if ret:
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        
        cv2.imshow('frame', fgmask)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        
    else:
        break
        
cap.release()
cv2.destroyAllWindows()