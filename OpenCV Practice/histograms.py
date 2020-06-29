import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(imgray, 'gray'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.hist(img.ravel(), 256, [0, 256]), plt.xlim([0, 256])

plt.subplot(224)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
	histr = cv2.calcHist([img], [i], None, [256], [0, 256])
	plt.plot(histr, color=col)
	plt.xlim([0, 256])

plt.show()