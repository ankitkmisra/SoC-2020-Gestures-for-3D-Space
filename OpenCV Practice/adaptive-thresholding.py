import cv2 as cv 
import numpy as np 

img = cv.imread('sudoku.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 6)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 6)

cv.imshow('Image', img)
cv.imshow('Th1', th1)
cv.imshow('Th2', th2)
cv.imshow('Th3', th3)

cv.waitKey(0)

cv.imwrite('sudoku_thresh_binary.png', th1)
cv.imwrite('sudoku_adaptive_thresh_mean.png', th2)
cv.imwrite('sudoku_adaptive_thresh_gaussian.png', th3)

cv.destroyAllWindows()