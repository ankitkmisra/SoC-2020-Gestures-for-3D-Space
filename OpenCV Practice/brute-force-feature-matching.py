import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('box.png', 0)
img2 = cv2.imread('box_in_scene.png', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], np.array([]), flags=2, matchColor=(0,0,255))

plt.imshow(img3)
plt.xticks([]), plt.yticks([])
plt.show()