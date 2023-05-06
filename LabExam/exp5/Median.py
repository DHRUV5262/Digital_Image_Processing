import cv2
import numpy as np
img=cv2.imread("salt&paperNoise.jpg")
img_median = cv2.medianBlur(img, 5)
cv2.imshow("image org", img)
cv2.imshow("image median",img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()
