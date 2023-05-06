import numpy as np
import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Minions", img)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("binary", thresh1)
cv2.imshow("binary inv", thresh2)
cv2.imshow("trunc", thresh3)
cv2.imshow("tozero", thresh4)
cv2.imshow("tozero inv", thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()
