import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blocks.jpg', 0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, np.array([]), color=(255,0,0))

print('Threshold: ', fast.getThreshold())
print('nonmaxSuppression: ', fast.getNonmaxSuppression())
print('neighborhood: ', fast.getType())
print('Total Keypoints with nonmaxSuppression: ', len(kp))

cv2.imwrite('fast_true.png', img2)

fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

print('Total Keypoints with nonmaxSuppression: ', len(kp))

img3 = cv2.drawKeypoints(img, kp, np.array([]), color=(255,0,0))

cv2.imwrite('fast_false.png', img3)