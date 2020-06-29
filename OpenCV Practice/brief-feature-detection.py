import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blocks.jpg', 0)

star = cv2.xfeatures2d.StarDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = star.detect(img, None)

kp, des = brief.compute(img, kp)

print(brief.getDescriptorSize())
print(des.shape)