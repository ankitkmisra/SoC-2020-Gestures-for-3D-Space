import cv2
import numpy as np 

img = cv2.imread('bolt.jpg', 0)

# rows,cols = img.shape
# M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
# img = cv2.warpAffine(img,M,(cols,rows))

ret, thresh = cv2.threshold(img, 50, 255, 0)

contours, heirarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

M = cv2.moments(cnt)

rows, cols = img.shape
print('lx = ', cols)
print('ly = ', rows)

print('cx = ', int(M['m10']/M['m00']))
print('cy = ', int(M['m01']/M['m00']))

area = cv2.contourArea(cnt)
print('area = ', area)

per = cv2.arcLength(cnt, True)
print('perimeter = ', per)

print(cv2.isContourConvex(cnt))

# epsilon = 0.08*per
# approx = cv2.approxPolyDP(cnt, epsilon, True)

hull = cv2.convexHull(cnt)

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 5)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (255, 255, 255), 15)

(x, y), radius = cv2.minEnclosingCircle(cnt)
centre = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, centre, radius, (255, 255, 255), 1)

cv2.drawContours(img, [cnt], 0, (255, 255, 255), 10)

cv2.imshow('img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()