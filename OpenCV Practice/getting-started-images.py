import cv2

img = cv2.imread('lena.jpg', 1)

print(img)

cv2.imshow('Lena', img)

x = cv2.waitKey(0)

if x == ord('s'):
	cv2.imwrite('lena_clone.png', img)

cv2.destroyAllWindows()