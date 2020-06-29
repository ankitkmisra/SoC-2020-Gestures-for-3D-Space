import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blocks.jpg', 0)

orb = cv2.ORB_create()

kp = orb.detect(img, None)

kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, np.array([]), (0,255,0), flags=0)
plt.imshow(img2, 'gray')
plt.show()