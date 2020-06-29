import cv2
import numpy as np 

img = cv2.imread('bolt.jpg', 0)

ret, thresh = cv2.threshold(img, 50, 255, 0)

contours, heirarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print(aspect_ratio)

area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area
print(extent)

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print(solidity)

equi_diam = np.sqrt(4*area/np.pi)
print(equi_diam)

(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print(angle)

mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
print(pixelpoints)