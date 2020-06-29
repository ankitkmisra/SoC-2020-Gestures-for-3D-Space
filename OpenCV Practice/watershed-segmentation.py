import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

plt.subplot(331), plt.imshow(gray, 'gray')
plt.title('Coins'), plt.xticks([]), plt.yticks([])
plt.subplot(332), plt.imshow(thresh, 'gray')
plt.title('Coins_Otsu'), plt.xticks([]), plt.yticks([])

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

plt.subplot(333), plt.imshow(opening, 'gray')
plt.title('Coins_Open'), plt.xticks([]), plt.yticks([])
plt.subplot(334), plt.imshow(sure_bg, 'gray')
plt.title('Coins_BG'), plt.xticks([]), plt.yticks([])

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

plt.subplot(335), plt.imshow(dist_transform, 'gray')
plt.title('Coins_DistT'), plt.xticks([]), plt.yticks([])
plt.subplot(336), plt.imshow(sure_fg, 'gray')
plt.title('Coins_FG'), plt.xticks([]), plt.yticks([])

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

plt.subplot(337), plt.imshow(unknown, 'gray')
plt.title('Coins_Unknown'), plt.xticks([]), plt.yticks([])

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

plt.subplot(338), plt.imshow(markers)
plt.title('Coins_Markers'), plt.xticks([]), plt.yticks([])

markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]

plt.subplot(339), plt.imshow(markers)
plt.title('Markers_Seg'), plt.xticks([]), plt.yticks([])

cv2.imshow('Result', img)
cv2.waitKey(0)

plt.show()

cv2.destroyAllWindows()