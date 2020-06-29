import cv2
import numpy as np
from matplotlib import pyplot as plt

imgorig = cv2.imread('lena.jpg')
img = cv2.cvtColor(imgorig, cv2.COLOR_BGR2GRAY)

hist, bins = np.histogram(img.ravel(), 256, [0, 256])

cdf = hist.cumsum()
cdf_norm = cdf*hist.max()/cdf.max()

plt.subplot(321), plt.imshow(img, 'gray'), plt.xticks([]), plt.yticks([])

plt.subplot(322), plt.plot(cdf_norm, color = 'b')
plt.hist(img.ravel(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]

img3 = cdf[imgorig]

hist, bins = np.histogram(img2.ravel(), 256, [0, 256])

cdf = hist.cumsum()
cdf_norm = cdf*hist.max()/cdf.max()

plt.subplot(323), plt.imshow(img2, 'gray'), plt.xticks([]), plt.yticks([])

plt.subplot(324), plt.plot(cdf_norm, color = 'b')
plt.hist(img2.ravel(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

plt.subplot(325), plt.imshow(cv2.cvtColor(imgorig, cv2.COLOR_BGR2RGB)), plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)), plt.xticks([]), plt.yticks([])

plt.show()

equ1 = cv2.equalizeHist(img)
equ2 = cv2.createCLAHE(clipLimit=1000.0, tileGridSize=(1,1)).apply(img)
cv2.imwrite('contrasts.png', np.hstack((img, equ1, equ2)))
cv2.destroyAllWindows()