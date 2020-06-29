import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

cv2.line(img, (0, 0), (400, 400), (0, 0, 255), 7)
cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 3)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)
cv2.rectangle(img, (0, 384), (128, 519), (0, 255, 0), -1)
cv2.circle(img, (255, 255), 25, (100, 150, 0), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV is fun!', (10, 500), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
cv2.ellipse(img, (255, 255), (100, 70), 30, 0, 270, (120, 120, 120), 1)

cv2.imshow('My Drawing', img)

cv2.waitKey(0)

cv2.imwrite('my_drawing.jpg', img)

cv2.destroyAllWindows()