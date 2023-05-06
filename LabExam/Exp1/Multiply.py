



import cv2
import numpy as np
img = cv2.imread("car.jpg")
img = cv2.resize(img, (512, 512))
matrix = np.ones(img.shape, dtype="uint8")*100
img_bri = cv2.multiply(img, matrix)
img_dark = cv2.subtract(img, matrix)
cv2.imshow("Original", img)
cv2.imshow("Bright", img_bri)
cv2.imshow("darker", img_dark)
cv2.waitKey(0)
cv2.destroyAllWindows()