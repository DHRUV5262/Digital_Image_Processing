import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("minions.jpg", 0)
img = cv2.resize(img, (512, 512))
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
equ = cv2.equalizeHist(img)
hist = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(hist)
res = np.hstack((img, equ))
plt.show()
cv2.imshow("Equalized image", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
