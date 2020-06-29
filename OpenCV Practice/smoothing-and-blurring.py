import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones([7, 7], np.float32)/49
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (7, 7))
gblur = cv2.GaussianBlur(img, (7, 7), 0)
mblur = cv2.medianBlur(img, 7)
bf = cv2.bilateralFilter(img, 7, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'gblur', 'mblur', 'bf']
images = [img, dst, blur, gblur, mblur, bf]

for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images[i], 'gray')
	plt.xticks([])
	plt.yticks([])

plt.show()