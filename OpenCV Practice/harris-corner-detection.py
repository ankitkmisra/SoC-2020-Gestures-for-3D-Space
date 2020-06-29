import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('chessboard.png')
img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()] = [0, 255, 0]

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()