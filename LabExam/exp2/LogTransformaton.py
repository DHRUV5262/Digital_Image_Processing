import cv2
import numpy as np
img = cv2.imread("minions.jpg")
res = 100*np.log10(1+img)
res = np.array(res, dtype=np.uint8)
cv2.imshow("Original image", img)
cv2.imshow("log transformation", res)
cv2.waitKey(0)
cv2.destroyAllWindows()