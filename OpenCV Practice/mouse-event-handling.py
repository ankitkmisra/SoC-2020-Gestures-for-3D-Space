import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, ' ', y)
		strxy = str(x) + ' ' + str(y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, strxy, (x, y), font, 0.5, (255, 255, 0), 2)
		cv2.imshow('my-image', img)
	if event == cv2.EVENT_RBUTTONDOWN:
		blue = img[y, x, 0]
		red = img[y, x, 1]
		green = img[y, x, 2]
		strbgr = str(blue) + ' ' + str(green) + ' ' + str(red)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, strbgr, (x, y), font, 0.5, (0, 255, 255), 2)
		cv2.imshow('my-image', img)

#img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('lena.jpg', 1)

cv2.imshow('my-image', img)

cv2.setMouseCallback('my-image', click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()